from collections import defaultdict
import bisect
from itertools import product

n = int(input())
s = input()

# {文字:その文字の出現位置}の辞書を構築
d = defaultdict(list)
for i in range(n):
    d[s[i]].append(i)

def canCreate(x,y,z):
    pos = 0
    for c in map(str, [x,y,z]):
        pos = bisect.bisect_left(d[c], pos)
        if pos == len(d[c]):
            return False
        pos = d[c][pos] + 1
    return True

ans = sum([canCreate(x, y, z) for x,y,z in product(range(10), repeat=3)])

print(ans)  