n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
ans=0

for x in range(0,n+1):
  a1sum=sum(a1[0:x+1])
  a2sum=sum(a2[x:n+1])
  ans=max(ans,a1sum+a2sum)
  
print(ans)
