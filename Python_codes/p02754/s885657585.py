n,a,b = map(int, input().split())
div = n//(a+b)
mod = n%(a+b)

if a>=mod:
  print((div*a)+mod)
else:
  print((div*a)+a)