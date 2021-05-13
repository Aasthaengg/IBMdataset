from itertools import permutations
N, C, *L = map(int, open(0).read().split())
ls =[[0]*(C+1) for i in range(3)]
D = L[:C*C]
X = L[C*C:]
for i in range(N):
  for j in range(N):
    c = X[i*N+j]
    ls[(i+j)%3][c] += 1
cost = [[0]*(C+1) for i in range(3)]
for i in range(3):
  n = sum(ls[i])
  for j in range(1,C+1):
    for h in range(1,C+1):
      cost[i][j] += D[(h-1)*C+j-1]*ls[i][h]
  
ans = 10**10
for l in permutations(range(1,C+1),3):
  ans = min(ans, sum(cost[i][l[i]] for i in range(3)))
print(ans)