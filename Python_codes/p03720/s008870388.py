import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()
from collections import defaultdict

d = defaultdict(int)
for i in range(M):
    a,b = MI()
    d[a] += 1
    d[b] += 1

for i in range(1,N+1):
    print(d[i])