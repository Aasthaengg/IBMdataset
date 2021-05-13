from math import gcd

mod = 10 ** 9 + 7
n = int(input())
iwashi = dict()
origin_iwashi = 0
for _ in range(n):
  a, b = map(int, input().split())
  if a == b == 0:
    origin_iwashi += 1
  elif a == 0:
    if (1, 0) in iwashi:
      iwashi[(1, 0)][1] += 1
    else:
      iwashi[(1, 0)] = [0, 1]
  elif b == 0:
    if (1, 0) in iwashi:
      iwashi[(1, 0)][0] += 1
    else:
      iwashi[(1, 0)] = [1, 0]
  else:
    if b < 0:
      a, b = -a, -b
    g = gcd(a, b)
    a //= g
    b //= g
    if a > 0:
      if (a, b) in iwashi:
        iwashi[(a, b)][0] += 1
      else:
        iwashi[(a, b)] = [1, 0]
    else:
      if (b, -a) in iwashi:
        iwashi[(b, -a)][1] += 1
      else:
        iwashi[(b, -a)] = [0, 1]
count = 1
for i, j in iwashi.values():
  tmp = pow(2, i, mod) + pow(2, j, mod) - 1
  count = count * tmp % mod
count = (count + origin_iwashi - 1) % mod
print(count)