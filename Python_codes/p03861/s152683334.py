a, b, x = map(int, input().split())

# a = p*x + r, b = q*x + s
p = a // x
r = a % x
q = b // x
s = b % x

res = q - p

if r == 0:
  res += 1

print(res)