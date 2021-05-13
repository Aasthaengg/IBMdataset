a,b = map(int,input().split())
def gcd(x,y):
  while y!=0:
    x,y = y,x%y
  return x
m = gcd(max(a,b),min(a,b))
print(a*b//m)