import fractions
from functools import reduce

def lcm(x, y):
  return (x * y) // fractions.gcd(x, y)

def lcm_for_lst(lst):
  return reduce(lcm, lst)

n = int(input())
lst = []
for i in range(n):
  t = int(input())
  lst.append(t)
print(lcm_for_lst(lst))