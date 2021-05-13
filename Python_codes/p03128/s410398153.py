N, M = map(int, input().split())
A = list(map(int, input().split()))

tab = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
A_cmp = {}
for Ai in sorted(A):
    A_cmp[tab[Ai]] = Ai
A = list(A_cmp.values())
A.sort(key=lambda x: -x)

memo = [None] * (N + 1)
memo[0] = 0

import sys
sys.setrecursionlimit(100000)

def dp(X):
    if X < 0: return -(1000000007)
    if memo[X] != None: return memo[X]
    #
    rets = []
    for i, Ai in enumerate(A):
        rets.append(dp(X - tab[Ai]) + 1)
    #
    ret = max(rets)
    memo[X] = ret
    return ret

ans_len = dp(N)

N_tmp = N
ans = ''
for i in range(ans_len):
    for j, Aj in enumerate(A):
        if dp(N_tmp) - 1 == dp(N_tmp - tab[Aj]):
            ans += str(Aj)
            N_tmp -= tab[Aj]
            break

print(ans)