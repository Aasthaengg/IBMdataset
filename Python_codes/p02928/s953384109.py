N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans = 0
for i in range(N):
  a = 0
  b = 0
  for j in range(N):
    if j < i and A[j] < A[i]:
      a += 1
    elif i < j and A[i] > A[j]:
      b += 1
  ans = (ans + ((K - 1) * a + (K + 1) * b) * K // 2) % mod
print(ans)