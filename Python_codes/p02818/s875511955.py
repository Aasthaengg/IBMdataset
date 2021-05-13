t,a,n=map(int,input().split())
if t-n<0:
  if a-(n-t)<0:
    a=0
    t=0
  else:
    a-=n-t
    t=0
else:
  t=t-n
  
print(t,a)