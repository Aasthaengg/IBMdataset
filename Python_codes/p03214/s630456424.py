from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()

ave=sum(a)/n
min_v=10**9
for i in range(n-1,-1,-1):
  if abs(a[i]-ave)<=min_v:
    min_v=abs(a[i]-ave)
    ans=i

print(ans)