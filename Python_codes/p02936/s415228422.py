from collections import defaultdict, deque
n,q = map(int,input().split())
dic = defaultdict(list)
for i in range(n-1):
    a,b = map(int,input().split())
    dic[b].append(a)
    dic[a].append(b)
# print(d)

dp = [-1]+[0]*n

for i in range(q):
    p,x = map(int,input().split())
    dp[p] += x

visited = [False]*(n+1)
que = deque([1])

while que:
    parent = que.popleft()
    visited[parent] = True
    for child in dic[parent]:
        if not visited[child]:
            dp[child] += dp[parent]
            que.append(child)

print(*dp[1:])