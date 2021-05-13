import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7




n, k, l = map(int, input().split())

table1 = [-1] * n
table2 = [-1] * n
def find(x, table):
    if table[x] < 0:
        return x
    table[x] = find(table[x], table)
    return table[x]


def union(x, y, table):
    r1 = find(x, table)
    r2 = find(y, table)
    if r1 == r2:
        return
    d1 = table[r1]
    d2 = table[r2]
    if d1 <= d2:
        table[r2] = r1
        if d1 == d2:
            table[r1] -= 1
    else:
        table[r1] = r2



for i in range(k):
    u, v = map(int, input().split())
    union(u - 1, v - 1, table1)


for i in range(l):
    u, v = map(int, input().split())
    union(u - 1, v - 1, table2)


f = defaultdict(int)
for i in range(n):
    f[(find(i, table1), find(i, table2))] += 1



print(*[f[(find(j, table1), find(j, table2))] for j in range(n)])