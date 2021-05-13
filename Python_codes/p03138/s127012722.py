N, K = map(int, input().split())
A = list(map(int, input().split()))
def digits_count(n):
  cnt = 0
  while n != 0:
    cnt += 1
    n //= 2
  return cnt
M = digits_count(max(max(A), K))
L = digits_count(K)
X = [0 for _ in range(M)] # 1 times per digits
B = [1 for _ in range(M)]
for i in range(M-1):
  B[i+1] = B[i] * 2
for i in range(M):
  for j in range(N):
    X[i] += A[j] % 2
    A[j] //= 2
S = 0
for i in range(L, M):
  S += B[i] * X[i]
def XXOR(m, n):
  if n == 0:
    val = 0
    for i in range(m):
      val += B[i] * X[i]
    return val
  else:
    d = (n // B[m-1]) % 2
    if d == 1:
      left = B[m-1] * X[m-1]
      for i in range(m-1):
        left += max(X[i], N - X[i]) * B[i]
      return max(XXOR(m-1, n - B[m-1]) + (N - X[m-1]) * B[m-1], left)
    else:
      return XXOR(m-1, n) + X[m-1] * B[m-1]
print(XXOR(L, K) + S)