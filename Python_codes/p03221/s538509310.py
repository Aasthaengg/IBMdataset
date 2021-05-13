import bisect
N,M = map(int, input().split())
q = [[int(j) for j in input().split()] for i in range(M)]
li = [[] for k in range(N+1)]

for i,j in sorted(q):
    li[i].append(j)

for p,y in q:
    z = bisect.bisect(li[p],y)
    print("{:0=6}".format(p) + "{:0=6}".format(z))