n,t=map(int,input().split())
x=1234
for i in range(n):
  c,d=map(int,input().split())
  if d<=t:
    if c<=x:
      x=c
if x==1234:
  print('TLE')
else:
  print(x)
    
