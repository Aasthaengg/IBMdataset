N,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
ans=0
for i in a:
  x-=i
  if x<0:
    break
  ans+=1
print(ans-(x>0))
