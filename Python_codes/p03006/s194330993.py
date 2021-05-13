import sys
from collections import Counter
n = int(input())
ls = []
if n == 1:
    print(1)
else:
    for i in range(n):
        x, y = [int(i) for i in sys.stdin.readline().split()]
        ls.append((x, y))
    res = []
    for i in range(n - 1):
        for j in range(i+1, n):
            res.append((ls[j][0] - ls[i][0], ls[j][1] - ls[i][1]))
            res.append((- ls[j][0] + ls[i][0], - ls[j][1] + ls[i][1]))
    ct = Counter(res)
    print(n - max(ct.values()))