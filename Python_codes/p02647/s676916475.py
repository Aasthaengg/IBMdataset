import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
As = list(mapint())
from itertools import accumulate

for _ in range(K):
    lamps = [0]*N
    for i, a in enumerate(As):
        lamps[max(0, i-a)] += 1
        if i+a+1<=N-1:
            lamps[i+a+1] -= 1
    As = list(accumulate(lamps))
    if sum(As)==N**2:
        break
print(*As)