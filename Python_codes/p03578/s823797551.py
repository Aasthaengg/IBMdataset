import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ds = list(mapint())
M = int(input())
Ts = list(mapint())

from collections import Counter
c = Counter(Ds)
for t in Ts:
    if c[t]==0:
        print('NO')
        break
    else:
        c[t] -= 1
else:
    print('YES')