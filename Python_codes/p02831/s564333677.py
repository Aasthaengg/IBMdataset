a,b=map(int,input().split())
def g(x,y):
  while y: x,y=y,x%y
  return x
print(a*b//g(a,b))