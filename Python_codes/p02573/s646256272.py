n, m = map(int, input().split())

# 隣接リストをつくる 
adj_list = [[] for i in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  adj_list[a].append(b)
  adj_list[b].append(a)
  
# どの連結成分に属してるかを把握するための配列
group = [-1 for i in range(n)]

# 各頂点 i から探索をする
for i in range(n):
  if group[i] != -1: continue
  # i から DFS
  newly_visited = [i]
  group[i] = i
  while len(newly_visited) > 0:
    now = newly_visited.pop()
    for j in adj_list[now]:
      if group[j] != -1: continue
      newly_visited.append(j)
      group[j] = i

hist = [0 for i in range(n)]
for g in group:
  hist[g] += 1
print(max(hist))
