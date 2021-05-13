t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
if (a1>b1 and a2>b2) or (b1>a1 and b2>a2):
  print(0)
elif abs(a1-b1)*t1>abs(a2-b2)*t2:
  print(0)
elif abs(a1-b1)*t1==abs(a2-b2)*t2:
  print('infinity')
else:
  d1=abs(a1-b1)*t1
  d2=abs(a2-b2)*t2
  l=0
  r=10**18+1
  while r-l!=1:
    mid=(l+r)//2
    if d1*(mid+1)-d2*mid<0:
      r=mid
    else:
      l=mid
  if d1*(l+1)-d2*l==0:
    print(2*l)
  else:
    print(2*l+1)