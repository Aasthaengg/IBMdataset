from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import Counter

n=int(input())
d=lnii()
m=int(input())
t=lnii()

c=Counter(d)
for i in t:
  if c[i]==0:
    print('NO')
    exit()
  else:
    c[i]-=1

print('YES')