N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
P, Q = [0]*(N+1), [0]*(M+1)
for i in range(N):
  P[i+1] = P[i]+A[i]
for i in range(M):
  Q[i+1] = Q[i]+B[i]
j, result = M, 0
for i in range(N+1):
  if P[i]>K:
    break
  if K-P[i]>=Q[j]:
    result = max(result, i+j)
  else:
    while 0<j and K-P[i]<Q[j-1]: j -= 1
    result = max(result, i+j-1)
print(result)