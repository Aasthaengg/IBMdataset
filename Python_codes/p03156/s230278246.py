n=int(input())
a,b=map(int,input().split())
x=list(map(int,input().split()))
t=0
u=0
v=0
for i in x:
  if i<=a:
    t+=1
  elif i<=b:
    u+=1
  else:
    v+=1
print(min(t,u,v))