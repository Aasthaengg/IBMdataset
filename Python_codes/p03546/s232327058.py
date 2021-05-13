def min_ind_except_for_fixed(seq, fixed):
  m = float('inf')
  ind = -1
  for i in range(len(seq)):
    if not fixed[i] and seq[i] < m:
      ind = i
      m = seq[i]
  return ind


def dijkstra_mat(adj_matrix, start, goal):
  V = len(adj_matrix)
  assert V == 10
  cost = [float('inf')] * V    # cost[i] = (minimum cost from node_start to node_i)
  cost[start] = 0
  fixed = [False] * V
  for _ in range(V):
    u = min_ind_except_for_fixed(cost, fixed)
    fixed[u] = True
    for j in range(V):
      cost[j] = min(cost[j], cost[u] + adj_matrix[u][j])
  return cost[goal]



h, w = map(int, input().split())
adj_matrix_weight = [list(map(int, input().split())) for _ in range(10)]

min_cost_change_to_1 = [dijkstra_mat(adj_matrix_weight, start=i, goal=1) for i in range(10)]
# print(min_cost_change_to_1)

total_min_cost = 0
for _ in range(h):
  line = list(map(int, input().split()))
  for num in line:
    if num != -1:
        total_min_cost += min_cost_change_to_1[num]

print(total_min_cost)
