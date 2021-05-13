n=int(input())
sy,sx=[0,0]
t1=0
ch=0

for _ in range(n):
  t,x,y=map(int,input().split())
  if (abs(sy-y)+abs(sx-x)-abs(t-t1))%2!=0 or abs(sy-y)+abs(sx-x)>abs(t-t1):
    ch+=1
  t1=t
  sy,sx=[y,x]
  
if  ch==0:
  print('Yes')
else:
  print('No')