# D - Lazy Faith

import bisect
INF = 10**18
A, B, Q = map(int, input().split())
S = [0]*A
T = [0]*B
X = [0]*Q
for i in range(A):
    S[i] = int(input())

for i in range(B):
    T[i] = int(input())

for i in range(Q):
    X[i] = int(input())

for x in X:
    #print(x)
    idxS = bisect.bisect_left(S, x)
    #print('idxS', idxS)
    if idxS==0:
        leftS = INF
        rightS = S[idxS] - x
    elif idxS==A:
        leftS = x - S[idxS-1]
        rightS = INF
    else:
        leftS = x - S[idxS-1]
        rightS = S[idxS] - x
    #print(leftS, rightS)
    idxT = bisect.bisect_left(T, x)
    if idxT==0:
        leftT = INF
        rightT = T[idxT] -x
    elif idxT==B:
        leftT = x - T[idxT-1]
        rightT = INF
    else:
        leftT = x - T[idxT-1]
        rightT = T[idxT] - x
    #print(leftT, rightT)
    ans = max(leftS, leftT)
    ans = min(ans, max(rightS, rightT))
    ans = min(ans, leftS * 2 + rightT)
    ans = min(ans, leftT * 2 + rightS)
    ans = min(ans, leftS + rightT * 2)
    ans = min(ans, leftT + rightS * 2)
    print(ans)