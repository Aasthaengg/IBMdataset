# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import math
import sys
input = sys.stdin.readline

D, G = map(int, input().split())
# print(D, G)
P = []
C = []
for i in range(D):
    p,  c = map(int, input().split())
    P.append(p)
    C.append(c)

INF = 10**15


def F(i, n, GetPoint):
    if i == D:
        if GetPoint >= G:
            return n, GetPoint
        else:
            return INF, INF

    PerPoint = (i+1)*100

    if GetPoint < G:
        ANS = INF, INF
        # ALL
        N, GP = F(i+1, n+P[i], GetPoint+PerPoint*P[i] + C[i])
        if N < ANS[0]:
            ANS = N, GP
        # through
        N, GP = F(i+1, n, GetPoint)
        if N < ANS[0]:
            ANS = N, GP

        # part
        # 上位合計
        PupperAll = sum([(j+1)*100*P[j] + C[j] for j in range(i+1, D)])
        rN = math.ceil((G - GetPoint - PupperAll)/PerPoint)
        if 0 < rN < P[i]:
            GP = GetPoint + PerPoint*rN + PupperAll
            N = n + rN + sum(P[i+1:])
            if N < ANS[0]:
                ANS = N, GP

        return ANS
    else:
        return n, GetPoint


print(F(0, 0, 0)[0])
