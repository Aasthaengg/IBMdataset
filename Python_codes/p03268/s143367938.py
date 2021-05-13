N, K = map(int, input().split())

n = N // K
ans = n**3

if K%2 == 0:
  m = N // (K//2)
  m = -(-m // 2)
  ans += m**3

print(ans)