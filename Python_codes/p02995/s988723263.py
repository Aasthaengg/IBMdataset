from fractions import gcd
A, B, C, D = map(int, input().split())
E = int(C * D / gcd(C, D))
def f(x):
  return (x - x // C - x // D + x // E)
print(f(B) - f(A-1))