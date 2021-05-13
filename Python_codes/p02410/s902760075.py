import sys

lines = [line for line in sys.stdin]

n,m = map(int,lines[0].split())

A=[map(int,lines[1+r].split()) for r in range(n)]
b=[int(lines[1+n+r]) for r in range(m)]

ab = []
for r in A:
    ab.append(0)
    for (a,c) in zip(r,b):
        ab[-1] += a*c

for i in ab:
    print (i)