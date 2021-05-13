N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
  m = N // i
  r = N % i
  ans += m * max(0, i-K)
  ans += max(0, r-K+1)

if K == 0:
  ans -= N
print(ans)
