n,x=map(int,input().split())
li=list(map(int,input().split()))
ans=1
l=0
for i in li:
  l+=i
  if l>x:
    break
  ans+=1
print(ans)