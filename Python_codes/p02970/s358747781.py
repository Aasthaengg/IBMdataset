n, d = map(int, input().split())
r = 2 * d + 1

if n % r == 0:
  obs = n // r
else:
  obs = n // r + 1

print(obs)