N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

s_A = sorted(A)

cost = 0
bought = 0
for n in range(N):
  if bought + s_A[n][1] < M:
    bought += s_A[n][1]
    cost += s_A[n][0]*s_A[n][1]
  else:
    cost += s_A[n][0]*(M-bought)
    break
    
print(cost)