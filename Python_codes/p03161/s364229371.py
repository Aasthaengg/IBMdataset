n, k  = map(int, input().split())
H = list(map(int, input().split()))

memo = [10**9 for _ in range(n)]
memo[0] = 0
for i in range(1, n):
  for j in range(1, k+1):
    if i - j >= 0:
      memo[i] = min(memo[i], memo[i-j] + abs(H[i] - H[i-j]))
print(memo[-1])