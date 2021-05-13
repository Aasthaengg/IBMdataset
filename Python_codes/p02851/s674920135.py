N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

if K == 1:
  print(0)
  exit()

L = [-1] * N
D = {}
D[A[0] % K] = 1
t = A[0] % K
L[0] = t
for i in range(1, min(K - 1, N)):
  t = (t + A[i] - 1) % K
  if t < 0:
    t += K
  if t in D:
    D[t] += 1
  else:
    D[t] = 1
  L[i] = t

n = 1
if n in D:
  ans = D[n]
else:
  ans = 0
for i in range(N):
  if L[i] != -1:
    D[L[i]] -= 1
  if i + K - 1 < N:
    t = (t + A[i + K - 1] - 1) % K
    if t < 0:
      t += K
    if t in D:
      D[t] += 1
    else:
      D[t] = 1
    L[i + K - 1] = t
  n = (n - 1 + A[i]) % K
  #n -= 1
  if n < 0:
    n += K
  if n in D:
    ans += D[n]
  
print(ans)