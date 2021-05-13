from logging import *
basicConfig(level=DEBUG, format='%(levelname)s: %(message)s')
disable(CRITICAL)

def solve():
    debug('k {} n {}'.format(k,n))
    debug('P {}'.format(P))
    debug('M {}'.format(M))
    can_positive = False
    if len(P) > 0:
        if k < n: can_positive = True
        else: can_positive = len(M)%2 == 0
    else: can_positive = k%2 == 0

    if can_positive:
        debug('positive')
        P.sort()
        M.sort(reverse = True)
        p0 = []
        if k%2: p0.append(P.pop())
        ar = []
        while len(P) >= 2: ar.append(P.pop() * P.pop())
        while len(M) >= 2: ar.append(M.pop() * M.pop())
        ar.sort(reverse = True)
        debug('p0 {}'.format(p0))
        debug('ar {}'.format(ar))
        debug('ar[:k] {}'.format(ar[:(k-k%2)//2]))
        return p0 + ar[:(k-k%2)//2]
    else: # can negative
        debug('negative')
        return sorted(P+M, key=lambda x: abs(x))[:k]


n, k = map(int, input().split())
P, M = [], [] # plus, minus
for a in map(int, input().split()):
    if a < 0: M.append(a)
    else: P.append(a)
ans, MOD = 1, 10**9 + 7
for a in solve(): ans *= a; ans %= MOD
ans += MOD; ans %= MOD
print(ans)
