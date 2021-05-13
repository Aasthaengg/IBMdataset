from itertools import *
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
for i,j,k in combinations(a,3):
    if i<j<k and i+j>k:
      ans+=1
print(ans)