N, M, K = map(int, input().split())
INF = int(1e18)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i, j = 0, 0
mcnt = 0
tmp = M+1
ccnt = 0
while tmp != 0:
  ccnt += 1
  tmp //= 2
LA = [0 for _ in range(N+1)]
LB = [0 for _ in range(M+1)]
for i in range(N):
  LA[i+1] = LA[i] + A[i]
for i in range(M):
  LB[i+1] = LB[i] + B[i]
for i in range(N+1):
  l, r = 0, M+1
  d = (l + r) // 2
  if LA[i] <= K:
    if LB[M] + LA[i] <= K:
      mcnt = max(i + M, mcnt)
    else:
      for j in range(ccnt + 1):
        if LB[d] + LA[i] <= K:
          l = d
          d = (l + r) // 2
        else:
          r = d
          d = (l + r) // 2
      mcnt = max(i + d, mcnt)
  else:
    break
print(mcnt)
