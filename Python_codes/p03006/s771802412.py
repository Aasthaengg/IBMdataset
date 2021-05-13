from sys import stdin
from itertools import combinations
from collections import Counter
n = int(stdin.readline().rstrip())
li = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
lin = list(combinations(li,2))
sa = []
for i,j in lin:
    p = i[0]-j[0]
    q = i[1]-j[1]
    sa.append((p,q))
    sa.append((-p,-q))
san = Counter(sa)
if n >= 2:
    print(n-max(san.values()))
else:
    print(1)