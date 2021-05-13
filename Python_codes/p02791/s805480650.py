n=int(input())
p=list(map(int,input().split()))
ans=0
now_min=n+1
for x in p:
  if now_min>=x:
    ans+=1
  now_min=min(now_min,x)
print(ans)