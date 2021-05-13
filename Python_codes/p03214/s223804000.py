N=int(input())
a=list(map(int,input().split()))
ave=sum(a)/N
deff=10**9
ans=0
for i in range(N):
  if abs(a[i]-ave)<deff:
    deff=abs(a[i]-ave)
    ans=i
print(ans)
