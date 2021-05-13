a,b,c=map(int,input().split())
def f(n):
  if(n==2000):
    return(c);
  return(a*(f(n-1))-b)
for i in range (2001,2011):
  print(f(i))