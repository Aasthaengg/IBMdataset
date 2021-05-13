from math import factorial as step
n,m=map(int,input().split())

def combination(n,r):
  if n < 0 or r < 0 or n-r<0:
    return 0
  return step(n) // (step(r) * step(n-r))

res = combination(n,2) + combination(m,2)
print(res)