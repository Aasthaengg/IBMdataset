import sys
from bisect import bisect_left

n,q = map(int, input().split())
lines = sys.stdin.readlines()
c = []
for line in lines[:n]:
    s,t,x = map(int, line.split())
    c.append((x,s,t))
c.sort()
d = list(map(int,lines[n:]))

ans = [-1] * q
skip = [-1] * q
for x,s,t in c:
    ss = bisect_left(d,s-x)
    tt = bisect_left(d,t-x)
    while ss < tt:
        if skip[ss] == -1:
            ans[ss] = x
            skip[ss] = tt
            ss += 1
        else:
            ss = skip[ss]
print(*ans,sep='\n')
