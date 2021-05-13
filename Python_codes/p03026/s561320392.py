import sys
import collections
input = sys.stdin.readline
N = int(input())
edge = [list(map(int,input().split())) for _ in range(N-1)]
c = sorted(list(map(int,input().split())),reverse=True)
graph = [[] for _ in range(N)]
ans = [-1 for _ in range(N)]
queue = collections.deque()

for e in edge:
    graph[e[0]-1].append(e[1]-1)
    graph[e[1]-1].append(e[0]-1)

for i in range(N):
    if len(graph[i])==1:
        queue.append(i)
        ans[i] = c[0]
        break
k=1
while queue:
    node = queue.popleft()
    for adj in graph[node]:
        if ans[adj]==-1:
            ans[adj] = c[k]
            k += 1
            queue.append(adj)
            
print(sum(c)-max(c))
print(*ans)