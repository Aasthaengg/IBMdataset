mod = 10**9+7
N = int(input())
A = list(map(int, input().split()))
ans = 0
i = 0
while i < 60:
  mask = 2**i
  n = sum([1 if a&mask > 0 else 0 for a in A])
  ans += n*(N-n)*pow(2, i, mod)
  ans %= mod
  i += 1
print(ans)