def main():
  n, m = input_list()
  s = input()
  t = input()
  gcm = fractions.gcd(n, m)
  lcm = (n*m)//gcm
  ng = n//gcm
  mg = m//gcm
  for i in range(gcm):
    if s[ng*i] != t[mg*i]:
      print(-1)
      exit(0)
  print(lcm)
  
def input_list():
  return list(map(int, input().split()))

def input_list_str():
  return map(str, input().split())

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

# 2で割り切れる回数
def divide_two(arg):
  c = 0
  while True:
    if c >= 2:
      break
    if arg % 2 != 0:
      break
    arg //= 2
    c += 1
  return c 

import math
import fractions
import collections
from functools import reduce
main()