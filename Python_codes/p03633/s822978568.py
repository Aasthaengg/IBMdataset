import sys
from fractions import gcd

read = sys.stdin.buffer.read

n,*t = list(map(int, read().split()))

def lcm(t):
  x = t[0]
  for i in range(1, len(t)):
    x = (x*t[i]) // gcd(x, t[i])
  return x

print(lcm(t))
