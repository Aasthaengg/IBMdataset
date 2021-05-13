from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m,x=nii()
a=lnii()

ans1=0
ans2=0
for i in a:
  if i<x:
    ans1+=1
  else:
    ans2+=1

print(min(ans1,ans2))