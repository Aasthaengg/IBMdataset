import math

k = int(input())
al = [int(x) for x in input().split()]

pmax = 2
pmin = 2
for a in reversed(al):
    pmin = a*math.ceil(pmin/a)
    pmax = a*math.floor(pmax/a) + a -1

if pmin > pmax:
    print(-1)
else:
    print(pmin, pmax)