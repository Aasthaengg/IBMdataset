def cycle_getter(N, start):
    """
    :param N: 移動回数
    :param start:　初期条件
    :return front: cycleまでの要素のリスト
            cycle: cycle内の要素のリスト
            end: cycle後の余った部分の要素のリスト
            cnt: cycle回数
    """
    p = start
    front, cycle, end = [], [], []
    cnt = 0
    visit = {p:0}
    L, R = N, -1
    P = [p]
    for i in range(1,N):
        p = lift(p)
        if p in visit:
            """
            (L, R) = (サイクルに入るまでに移動した回数, サイクルの終端に着くまでに移動した回数)
            [6,2,3,4,0,1,2] ⇒ (L, R) = (1, 6)
            """
            L, R = visit[p], i
            period = R-L
            break
        visit[p] = i
        P.append(p)
    front = P[:L]
    if L != N:
        cycle, end = P[L:R], P[L:L+(N-L)%period]
        cnt = (N-L)//period
    return front, cycle, end, cnt

################################################################################


import sys
input = sys.stdin.readline
from itertools import accumulate

def lift(x): return P[x-1]

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
res = -float("inf")
for i in range(1,N+1):
    front, cycle, end, cnt = cycle_getter(K,i)
    S = sum(C[j-1] for j in front)
    T = sum(C[j-1] for j in cycle)
    if cycle+end:
        U = max(0, max(accumulate(C[j-1] for j in cycle+end)))
    else: U=0
    if front:
        R = max(accumulate(C[j-1] for j in front))
    else: R=0
    res = max(res, S+T*(cnt-1)+U, S+U, R)
print(res)