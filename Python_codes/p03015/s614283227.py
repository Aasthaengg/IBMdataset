def power(a, p, mod):
  res = 1
  pwr = a
  while p > 0:
    if p & 1:
      res = res * pwr % mod
    pwr = pwr * pwr % mod
    p >>= 1
  return res

mod = 10**9 + 7

l = [int(bit) for bit in input()]
bl = len(l)
inv3 = power(3, mod-2, mod)
pow2 = 1
pow3 = power(3, bl-1, mod)
count = 0

for i in range(bl-1):
  if l[i]:
    count = (count + pow2 * pow3) % mod
    pow2 = pow2 * 2 % mod
  pow3 = pow3 * inv3 % mod
if l[-1]:
  count = (count + pow2 * 3) % mod
else:
  count = (count + pow2) % mod

print(count)