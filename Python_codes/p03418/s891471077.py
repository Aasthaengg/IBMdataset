N, K = list(map(int, input().split()))
ans = 0
for b in range(K + 1, N + 1):
  q = N // b
  r = N % b
  ans += q * (b - K) - (K == 0) + max(r - K + 1, 0)
print(ans)