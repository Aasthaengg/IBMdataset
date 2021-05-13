H, W = map(int, input().split())
C = [list(map(int, input().split())) for i in range(10)]
A = [list(map(int, input().split())) for i in range(H)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################

cost = warshall_floyd(C)

num = [0] * 10
for i in range(H):
  for j in range(W):
    if A[i][j] != -1:
      kazu = A[i][j]
      num[kazu] += 1
#print(num)
ans = 0
for i in range(10):
  ans += num[i] * cost[i][1]

print(ans)