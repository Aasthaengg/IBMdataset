from collections import deque

def bfs(graph, visited, ss):
  queue = deque([ss])
  visited[ss] = 0
  ans = [0]*n
  while queue:
    s = queue.popleft()
    for new_s in graph[s] :
      if visited[new_s] == -1:
        #　移動回数の計算
        visited[new_s] = visited[s] + 1
        queue.append(new_s)
        ans[new_s] = s
  return ans

n,m = map(int,input().split())
graph = [[] for j in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [-1]*n
ans = bfs(graph, visited, 0)

print('Yes')
for i in range(1,n) :
  print(ans[i]+1)