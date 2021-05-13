n,d=map(int,input().split())
a=2*d+1
if n%a==0:
  print(int(n/a))
else: 
  print(int(n/a)+1)