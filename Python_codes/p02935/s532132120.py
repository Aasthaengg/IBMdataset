from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
v=lnii()
v.sort()

ans=v[0]
for i in range(1,n):
  ans=(ans+v[i])/2

print(ans)