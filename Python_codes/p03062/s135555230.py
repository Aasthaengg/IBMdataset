n=int(input())
a=list(map(int,input().split()))
m=10**9
cnt=0
ans=0
for i in a:
  m=min(abs(i),m)
  ans+=abs(i)
  if i<0:cnt+=1
if cnt%2:ans-=2*m
print(ans)