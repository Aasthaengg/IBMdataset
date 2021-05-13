from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b=nii()
ans=0
for i in range(a,b+1):
  s=str(i)
  if s==s[::-1]:
    ans+=1

print(ans)