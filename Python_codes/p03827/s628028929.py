from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
s=input()

x=0
ans=0
for i in s:
  if i=='I':
    x+=1
  else:
    x-=1
  ans=max(ans,x)

print(ans)