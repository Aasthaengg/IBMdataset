N = int(input())
a = sorted(list(map(int,input().split())))
import fractions
from functools import reduce
def cal_gcd(numbers):
  return reduce(fractions.gcd, numbers)
print(cal_gcd(a))
