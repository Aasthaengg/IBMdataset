# 約数の数 = 素因数分解して、各素因数の(指数 + 1)をかけ合わせたもの
# 例：12 = 2^2 * 3^1 -> 3 * 2 = 6 (1,2,3,4,6,12)
# これが75になるためには、以下のペアを作れる必要がある。この組み合わせを数える
# 75 : 指数が74
# 3 * 25 : 指数が2 , 24
# 5 * 15 : 指数が4 , 14
# 3 * 5 * 5 : 指数が2,4,4

import sys
readline = sys.stdin.readline

N = int(readline())

def factorization(n):
  res = []
  temp = n
  for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
    if temp % i == 0:
      cnt = 0
      while temp % i == 0:
        cnt += 1
        temp //= i
      res.append([i,cnt])
  if temp != 1:
    res.append([temp, 1])
  if res == []:
    res.append([n, 1])
  return res

from collections import defaultdict
dic = defaultdict(int)
for i in range(1, N + 1):
  res = factorization(i)
  for r in res:
    dic[r[0]] += r[1]

ans = 0

vals = dic.values()
# 74以上のものを探す
i74 = 0
for v in vals:
  if v >= 74:
    i74 += 1
ans += i74

i2 = 0
i24 = 0
# 2,24以上のものを探す
for v in vals:
  if v >= 24:
    i24 += 1
  elif v >= 2:
    i2 += 1
ans += (i24 * (i24 - 1))
ans += i24 * i2
  
# 5,15以上のものを探す
i4 = 0
i14 = 0
for v in vals:
  if v >= 14:
    i14 += 1
  elif v >= 4:
    i4 += 1
ans += (i14 * (i14 - 1))
ans += i14 * i4

# 2,4,4を探す
i4 = 0
i2 = 0
for v in vals:
  if v >= 4:
    i4 += 1
  elif v >= 2:
    i2 += 1
if i4 >= 3:
  ans += ((i4 * (i4 - 1)) // 2) * (i4 - 2)
ans += ((i4 * (i4 - 1)) // 2) * i2

print(ans)