n = int(input())
from sys import exit
if n == 1:
  print(0)
  exit()

from collections import defaultdict as dd
dic_list = [{}, {}, {2: 1}]
def prime_factrization(num):  
  dic = dd(lambda: 0)
  for i in range(2, int(num**0.5) + 2):
    mod = num % i
    while mod == 0:
      num //= i
      dic[i] += 1
      mod = num % i
    if num == 1:
      break
  else:
    if num != 1:
      dic[num] += 1
  return dic

dic = dd(lambda: 0)
for i in range(2, n+1):
  pf = prime_factrization(i)
  for j in range(2, 100):
    dic[j] += pf[j]
#print(dic)

#75 = 5 * 5 * 3
up3_divisor = 0
for num in dic.values():
  if num >= 2:
    up3_divisor += 1
up5_divisor = 0
for num in dic.values():
  if num >= 4:
    up5_divisor += 1
up15_divisor = 0
for num in dic.values():
  if num >= 14:
    up15_divisor += 1
up25_divisor = 0
for num in dic.values():
  if num >= 24:
    up25_divisor += 1
up75_divisor = 0
for num in dic.values():
  if num >= 74:
    up75_divisor += 1

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans = 0
if up75_divisor >= 1:
  ans += combinations_count(up75_divisor, 1) #75
if up25_divisor >= 1:
  ans += combinations_count(up25_divisor, 1) * (combinations_count(up3_divisor, 1) - 1) #25 * 3
if up15_divisor >= 1:
  ans += combinations_count(up15_divisor, 1) * (combinations_count(up5_divisor, 1) - 1) #15 * 5
if up5_divisor >= 2:
  ans += combinations_count(up5_divisor, 2) * (combinations_count(up3_divisor, 1) - 2) #5 * 5 * 3
print(ans)