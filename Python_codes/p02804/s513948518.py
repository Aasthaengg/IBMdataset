import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
As = list(mapint())
mod = 10**9+7
As.sort()

pos = {}
neg = {}
pos[0] = 1
neg[0] = 1
for i in range(1, 10**5+3):
    pos[i] = (pos[i-1]*i)%mod
    neg[i] = pow(pos[i], mod-2, mod)

mini = 0
maxi = 0
for i, a in enumerate(As):
    if i<=N-K:
        mini += a*pos[(N-i-1)]*neg[K-1]*neg[N-i-K]
        mini %= mod
    if i>=K-1:
        maxi += a*pos[i]*neg[K-1]*neg[i-K+1]
        maxi %= mod
print((maxi-mini)%mod)