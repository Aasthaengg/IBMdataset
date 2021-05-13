a, b, n = [int(x) for x in input().split()]
def f(x):
  return a*x//b - a *(x//b)
print(f(min(b - 1, n)))
