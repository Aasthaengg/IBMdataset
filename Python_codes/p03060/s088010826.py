from operator import itemgetter
import sys
sys.setrecursionlimit(1000000)
ans=0

n=int(input())
v=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
for i in range(n):
    k=v[i]-c[i]
    if k>0:
        ans+=k
        
print(ans)
