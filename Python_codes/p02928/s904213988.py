N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7
L = [0 for _ in range(N)]
R = [0 for _ in range(N)]

for i in range(N):
  num = A[i]
  for j in range(i):
    if num > A[j]:
      L[i] += 1
  for k in range(i, N):
    if num > A[k]:
      R[i] += 1

answer = 0
for i in range(N):
  answer = (answer + L[i]*K*(K-1)//2%MOD + R[i]*K*(K+1)//2%MOD)%MOD
print(answer)