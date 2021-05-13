N=int(input())
A=list(map(int,input().split()))
import itertools
ans=0
for key,g in itertools.groupby(A):
  ans+=len(list(g))//2
print(ans)