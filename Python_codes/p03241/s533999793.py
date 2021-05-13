import sys
def factors(n):
  a = []
  x = 1
  while x * x <= n :
    if n % x == 0:          
      a.append(x)
      a.append(n//x)
    x += 1
  return a
n,m=map(int,input().split())
fac=factors(m)
fac.sort()
for i in range(len(fac)-1,-1,-1):
  if n*fac[i]<=m:
    print(fac[i])
    sys.exit()