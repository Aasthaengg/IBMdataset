n,a,b=map(int,input().split())
if b<a:
  print(0)
  exit()
  
if a==b:
  print(1)
  exit()
  

n-=2

if n<0:
  print(0)
  exit()

if n==0:
  print(1)
  exit()

print(b*n-a*n+1)
