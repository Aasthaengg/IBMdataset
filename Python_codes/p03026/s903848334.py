import heapq
import sys
sys.setrecursionlimit(10**7)
n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
c = [-i for i in list(map(int,input().split()))]
heapq.heapify(c)
print(-sum(c)+min(c))

for i in range(n):
    if len(g[i]) == 1:
        start = i
        break

ans = [-1]*n
ans[start] = -heapq.heappop(c)
q = [start]

while q:
    now = q.pop(-1)
    for i in g[now]:
        if ans[i] == -1:
            ans[i] = -heapq.heappop(c)
            q.append(i)

for i in ans:
    print(i)