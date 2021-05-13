n=int(input())
a=list(map(int,input().split()))
ans=0
cnt=-1
for i in range(1,n):
  if a[i-1]==a[i]:
    a[i]=cnt
    cnt-=1
    ans+=1
print(ans)
