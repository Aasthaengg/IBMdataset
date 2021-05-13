from collections import deque


n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]
c = list(map(int, input().split()))
c = sorted(c, reverse=True)

tree = [[] for i in range(n)]
cnt = [0] * n
for i in range(n - 1):
    a, b = info[i]
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
    cnt[a] += 1
    cnt[b] += 1

for i in range(n):
    if len(tree[i]) == 1:
        root = i
        break
        
q = deque([root])
visited = [False] * n
visited[root] = True
ind = 0
ans = 0
res = [0] * n
while q:
    v= q.pop()
    tmp_cnt = 0
    for nxt_v in tree[v]:
        if visited[nxt_v]:
            tmp_cnt += 1
    ans += c[ind] * tmp_cnt
    res[v] = c[ind]
    ind += 1
    for nxt_v in tree[v]:
        if visited[nxt_v]:
            continue
        visited[nxt_v] = True
        q.append(nxt_v)
    
print(ans)
print(*res)