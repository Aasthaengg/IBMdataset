x,y=map(int,input().split())
ans=1
for i in range(1000):
  x=x*2
  ans+=1
  if x>=y:
    break
print(ans+(0 if x==y else (-1)))