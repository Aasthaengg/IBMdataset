n,m = map(int, input().split())

def f(x):
  return x*(x-1)//2

print(f(n) + f(m))