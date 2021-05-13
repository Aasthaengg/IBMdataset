from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()
a.sort()

sum_v=0
ans=0
for i in range(n-1):
  sum_v+=a[i]
  if sum_v*2>=a[i+1]:
    ans+=1
  else:
    ans=0

ans+=1
print(ans)