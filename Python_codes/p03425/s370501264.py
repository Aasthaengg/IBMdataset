from itertools import combinations as cmbs
from sys import stdin
c = {"M":0,"A":0,"R":0,"C":0,"H":0}
for si in map(lambda s:s[0],stdin):
    if si in c:
        c[si] += 1
print(sum(i*j*k for i,j,k in cmbs(c.values(),r=3)))
