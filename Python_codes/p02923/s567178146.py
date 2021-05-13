n=int(input())
l=list(map(int,input().split()))

cnt=0
ans=0

lis=[(l[i+1]-l[i]) for i in range(n-1)]

for i in lis:
  if i<=0:
    cnt+=1
  else:
    ans=max(cnt, ans)
    cnt=0
    
ans=max(cnt, ans)
    
print(ans)