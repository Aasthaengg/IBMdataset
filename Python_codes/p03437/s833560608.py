import fractions
def lcm(a,b):
  return a*b/fractions.gcd(a,b)
x,y=map(int,input().split())
a=lcm(x,y)
if x%y==0:
  print(-1)
else:
  b=1
  while True:
    b+=1
    c=x*b
    if c%y!=0:
      print(c)
      break