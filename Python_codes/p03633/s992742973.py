from fractions import gcd
N = int(input())
l = [int(input()) for _ in range(N)]

def lcm(l):
  x = l[0]
  for i in range(1, len(l)):
    x = (x * l[i]) // gcd(x, l[i])
  return x

print(lcm(l))