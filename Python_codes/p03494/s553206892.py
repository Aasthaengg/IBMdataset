n=int(input())
a=list(map(int,input().split()))
ans,cnt=36,0
for i in range(n):
  while a[i]%2==0:
    a[i]//=2
    cnt+=1
  ans=min(ans,cnt)
  cnt=0
print(ans)
