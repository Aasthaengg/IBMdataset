n=int(input())
p=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
  pre=p[i-1]
  cur=p[i]
  nex=p[i+1]
  if (pre<cur and cur<nex) or(pre>cur and cur>nex):
    ans+=1
print(ans)