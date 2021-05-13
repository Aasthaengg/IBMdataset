N, M, X = map(int, input().split())
A= []
for i in range(N):
  temp = list(map(int, input().split()))
  A.append(temp)

uds = [0]*M
cost = 0
ans = -1

for bit in range(2**N):
  for i in range(N):
    if (bit >> i) & 1:
      cost += A[i][0]
      for j in range(M):
        uds[j] += A[i][j+1]
  if min(uds) >= X:
    if ans == -1 or ans > cost:
      ans = cost
  cost = 0
  uds = [0]*M

print(ans)