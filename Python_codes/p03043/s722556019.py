N, K = map(int, input().split())
ans = 0.0
for n in range(1, N+1):
  m = n
  a = 1
  while m < K:
    m <<= 1
    a /= 2
  ans += a
print(ans / N)