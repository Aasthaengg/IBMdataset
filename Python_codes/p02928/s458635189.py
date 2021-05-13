import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
As = list(mapint())
sortedAs = sorted(As)
mod = 10**9+7

cnt = 0
for i in range(N):
    for j in range(N-1, i, -1):
        if As[j-1]>As[j]:
            As[j-1], As[j] = As[j], As[j-1]
            cnt += 1

from bisect import bisect_right
dub = 0
for a in As:
    bigger = N-bisect_right(sortedAs, a)
    dub += ((K-1)*K//2)*bigger
    dub %= mod
print((cnt*K + dub)%mod)
