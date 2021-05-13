n,x=map(int, input().split())
l=list(map(int, input().split()))
cnt=0
ans=1
for i in range(n):
  if cnt+l[i]<=x:
    ans+=1
    cnt+=l[i]
  else:
    break
print(ans)