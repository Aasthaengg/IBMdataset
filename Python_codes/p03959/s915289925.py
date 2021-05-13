import sys
N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
if N == 1 and T[0] != A[0]:
    print(0)
    sys.exit()
INF = 10**13
minH = [1]*N
maxH = [INF]*N
pre_ti = 0
MOD = 10**9 + 7
for i, ti in enumerate(T):
    if ti > pre_ti:
        minH[i] = ti
        maxH[i] = ti
    else:
        maxH[i] = min(ti, maxH[i])
    pre_ti = ti
pre_ai = 0
for i, ai in enumerate(A[::-1], 1):
    if ai > pre_ai:
        minH[-i] = ai
        maxH[-i] = ai
    else:
        maxH[-i] = min(ai, maxH[-i])
    pre_ai = ai

ans = 1
for lh, uh in zip(minH, maxH):
    if lh > uh:
        ans = 0
        break
    ans = (ans * (uh-lh+1)) % MOD
print(ans)