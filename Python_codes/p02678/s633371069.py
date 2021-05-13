from collections import deque
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

q = deque([0])
d = [-1]*n
d[0] = 0
ans = [0]*n
print("Yes")

while q:
    p = q.popleft() # 先に入れた要素を取り出す
    for node in g[p]:
        if d[node] == -1:
            d[node] = d[p] + 1
            q.append(node) # リストへの追加
        else:
            if d[node] + 1 == d[p]: # 深さdに対してd+1の関係であるかのチェック
                ans[p] = node + 1

for i in range(1,n):
    print(ans[i])
