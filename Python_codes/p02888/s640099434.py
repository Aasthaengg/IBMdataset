import itertools
import bisect

n=int(input())
l=list(map(int,input().split()))

l.sort()
ans=0

for lst in itertools.combinations(range(n-1),2):
  a=l[lst[0]]
  b=l[lst[1]]
  ans+=bisect.bisect_left(l,a+b)-(lst[1]+1)


print(ans)