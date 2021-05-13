import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
mod = 10**9+7
from itertools import accumulate
lis = list(accumulate([0]+[i for i in range(N+1)]))
ans = 0
for k in range(K, N+2):
    MIN = lis[k]
    MAX = lis[-1]-lis[-1-k]
    ans += (MAX-MIN+1)
    ans %= mod
print(ans)