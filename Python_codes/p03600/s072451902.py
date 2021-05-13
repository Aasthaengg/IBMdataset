import copy
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
B = A

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
               # if d[i][j] == d[i][k] + d[k][j]:
               #   if (i != k) and (j != k):
               #     ans += d[i][j]
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################

#d = [[float("inf") for i in range(10)] for i in range(10)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
#for i in range(10):
#  for j in range(10):
#    d[i][j] = C[i][j]

#print(warshall_floyd(d))
#print(warshall_floyd(C))
B = copy.deepcopy(A)
cost = warshall_floyd(B)
#print(cost , A)

ans = 0
for i in range(N):
  for j in range(N):
    if cost[i][j] < A[i][j]:
      print("-1")
      quit()

for i in range(N):
  cost[i][i] = 10 ** 18
for i in range(N):
  for j in range(N):
    p = 1
    for k in range(N):
      if cost[i][j] >= cost[i][k] + cost[k][j]:
        p = 0
        break
    if p == 1:
      ans += cost[i][j]


ans = ans / 2
#for i in range(10):
#  ans += num[i] * cost[i][1]

print(int(ans))