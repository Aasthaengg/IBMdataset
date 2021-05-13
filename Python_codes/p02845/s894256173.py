from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()

l=[0,0,0]

mod=10**9+7

ans=1
for i in a:
  l_cnt=l.count(i)
  ans*=l_cnt
  ans%=mod
  for j in range(3):
    if l[j]==i:
      l[j]+=1
      break

print(ans)