from math import gcd
A, B, C, D = map(int, input().split())

def lcm(c, d):
  return c * d // gcd(c, d)

def divc(x):
  """ [A, B]にxの倍数がいくつあるかを返す"""
  b = B // x
  r = B % x
  a = A // x
  s = A % x
  res = b - a
  if s == 0:
    res += 1
  return res

ans = B - A + 1 - (divc(C) + divc(D) - divc(lcm(C, D)))

print(ans)