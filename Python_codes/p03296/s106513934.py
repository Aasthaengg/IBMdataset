n=int(input())
a=list(map(int,input().split()))
x=a[0]
cnt=0
ans=0
for i in a:
  if x!=i:
    ans+=cnt//2
    cnt=1
    x=i
  else:
    cnt+=1
ans+=cnt//2
print(ans)
