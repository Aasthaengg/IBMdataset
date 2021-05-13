import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
cAB = Counter()
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    cAB[a] += 1
    cAB[b] += 1
print('YES' if all([cAB[key]%2==0 for key in cAB.keys()]) else 'NO')