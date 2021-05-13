n = int(input())
graph = [[] for _ in range(n)]

global time
global visited 
global f_time 
global e_time 

time = 1
visited = [0 for _ in range(n)]
f_time = [0 for _ in range(n)]
e_time = [0 for _ in range(n)]

def input_graph(n):
  for _ in range(n):
    node_id, num, *v = list(map(int, input().split()))
    for i in range(num):
      graph[node_id-1].append(v[i]-1)

def dfs(node_id):
  global time
  f_time[node_id] = time
  time += 1

  for ad_node in graph[node_id]:
    if visited[ad_node] == 1:
      continue
    visited[ad_node] = 1
    dfs(ad_node)

  e_time[node_id] = time
  time += 1



if __name__ == "__main__":
  input_graph(n)
  for i in range(n):
    if visited[i] == 1:
      continue
    visited[i] = 1
    dfs(i)

  for i, (f, e) in enumerate(zip(f_time, e_time)):
    print(i+1, f, e)
  
  
