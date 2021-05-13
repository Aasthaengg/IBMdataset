from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import deque

n=int(input())
a=lnii()

ans=deque([])
for i in range(n):
  if i%2==0:
    ans.appendleft(a[i])
  else:
    ans.append(a[i])

if n%2==0:
  ans=reversed(ans)

print(*list(ans))