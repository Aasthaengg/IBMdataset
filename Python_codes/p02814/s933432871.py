from fractions import gcd
from functools import reduce
import sys

N, M = map(int,input().split())
an = list(map(lambda x: int(x)//2,input().split()))

time = 0

def myfunc(x):
  cnt = 0
  while True:
    if x%2!=0:break
    x = x//2
    cnt += 1
  return cnt

f0 = myfunc(an[0])

for a in an[1:]:
  if myfunc(a) != f0:
    print(0)
    sys.exit()

lcm = reduce(lambda x, y: (x*y)//gcd(x,y),an)
if lcm > M:
  print(0)
  sys.exit()
print((M//lcm +1)//2)