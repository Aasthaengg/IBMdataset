from itertools import accumulate
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=[0]*(2*a[0]+1)
for i in range(n):
  b[a[i]]+=1
b=list(accumulate(b[::-1]))[::-1]
s=list(accumulate([0]+a))
ok=0
ng=2*a[0]+1
while ng-ok>1:
  mid=(ng+ok)//2
  cnt=0
  for i in range(n):
    cnt+=b[max(0,mid-a[i])]
  if cnt>=m:
    ok=mid
  else:
    ng=mid
cnt=0
ans=0
for i in range(n):
  t=min(b[max(0,ng-a[i])],m-cnt)
  ans+=s[t]+a[i]*t
  cnt+=t
ans+=(m-cnt)*ok
print(ans)