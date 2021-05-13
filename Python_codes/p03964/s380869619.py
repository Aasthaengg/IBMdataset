n=int(input())
for i in range(n):
  if i==0:
    t,a=map(int,input().split())
  else:
    x,y=map(int,input().split())
    p=(t+x-1)//x
    q=(a+y-1)//y
    r=max(p,q)
    t,a=x*r,y*r
print(t+a)