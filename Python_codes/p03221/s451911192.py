import bisect
import collections
N,M = map(int, input().split())
q = [[int(j) for j in input().split()] for i in range(M)]
li = collections.defaultdict(list)

for i,j in sorted(q):
    li[i].append(j)

for p,y in q:
    z = bisect.bisect(li[p],y)
    print("{:0=6}".format(p) + "{:0=6}".format(z))