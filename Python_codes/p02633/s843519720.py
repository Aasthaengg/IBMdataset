from sys import stdin
x = int(stdin.readline().rstrip())

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
def lcm(a, b):
  return a * b // gcd(a, b)

ans = int(lcm(x, 360) / x)
print(ans)