import math 
n,a,b = map(int,input().split())
if a>b:
  print(0)
  exit()
if n==1 and a!=b:
  print(0)
  exit()
if n==2:
  print(1)
  exit()
q = b*(n-2)-a*(n-2)+1
print(q)