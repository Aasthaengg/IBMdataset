from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
global Q, S, T
global visited, dis
Q = deque([0])
S = [0] #訪れた順
T = []
visited = [0 for _ in range(n)]
dis = [-1 for _ in range(n)] #初めからの距離
visited[0] = 1
dis[0] = 0
def input_graph(n):
  for _ in range(n):
    node_id, num, *v = list(map(int, input().split()))
    for i in range(num):
      graph[node_id-1].append(v[i]-1)

def bfs(node_id):
  global Q, S
  while Q:
    node_id = Q.popleft()

    for ad_node in graph[node_id]:
      if visited[ad_node] == 1:
        continue
      visited[ad_node] = 1
      dis[ad_node] = dis[node_id] + 1
      S.append(ad_node)
      Q.append(ad_node)

if __name__ == "__main__":
  input_graph(n)
  bfs(0)
  for i, d in enumerate(dis):
    print(i+1, d)


