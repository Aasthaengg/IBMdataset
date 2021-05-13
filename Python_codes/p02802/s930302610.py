import numpy as np

N, M = map(int, input().split())

P = []
S = []

for _ in range(M):
    p, s = input().split()
    P.append(int(p))
    S.append(s)

AC = np.zeros(N)
WA = np.zeros(N)

for i in range(M):
    if AC[P[i]-1] == 0:
        if S[i] == 'WA':
            WA[P[i]-1] += 1
        else:
            AC[P[i]-1] += 1

WA[AC == 0] = 0

print(int(sum(AC)), int(sum(WA)))