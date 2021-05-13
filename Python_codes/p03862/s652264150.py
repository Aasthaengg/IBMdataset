n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(1,n):
  t_sum=a[i]+a[i-1]
  tt=0
  if t_sum>x:
    tt=t_sum-x
    tmp1=min(a[i],tt)
    ans+=tmp1
    a[i]-=tmp1
    tt-=tmp1
    if tt>0:
    # if i!=0:
      tmp2=min(a[i-1],tt)
      ans+=tmp2
      a[i-1]-=tmp2
print(ans)