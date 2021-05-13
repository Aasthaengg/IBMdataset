N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]

cost0 = []
cost1 = []
cost2 = []
indices = [2, 0, 1]
for color in range(C):
  cost = [0, 0, 0]
  for i in range(N):
    idx = indices[i%3]
    for j in range(N):
      cost[idx] += D[c[i][j]-1][color]
      idx = (idx + 1) % 3
  cost0.append([cost[0], color])
  cost1.append([cost[1], color])
  cost2.append([cost[2], color])

cost0.sort()
cost1.sort()
cost2.sort()
ans = float('inf')
for i in range(3):
  for j in range(3):
    for k in range(3):
      if len(set([cost0[i][1], cost1[j][1], cost2[k][1]])) == 3:
        ans = min(ans, cost0[i][0]+cost1[j][0]+cost2[k][0])

print(ans)