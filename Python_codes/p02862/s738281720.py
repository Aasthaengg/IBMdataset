X, Y = map(int, input().split())
mod = 10 ** 9 + 7
m = mod - 2
bin_m = []
while m:
  bin_m.append(m % 2)
  m >>= 1
p = 2 * X - Y
q = -X + 2 * Y
if p >= 0 and q >= 0 and p % 3 == 0:
  a = p // 3
  b = q // 3
  n = a + b
  ANS = 1
  for i in range(1, a+1):
    ANS = (ANS * (n+1-i)) % mod
    inv = 1
    for j in reversed(bin_m):
      inv = (inv * inv) % mod
      if j == 1:
        inv = (inv * i) % mod
    ANS = (ANS * inv) % mod
  print(ANS)
else:
  print(0)