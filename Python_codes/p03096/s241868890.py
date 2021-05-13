from collections import defaultdict

M = 10**9 + 7
N = int(input())
C = [0]*N
for i in range(N):
    C[i] = int(input())

P = [0]*N
Q = [0]*N
QS = defaultdict(int)
Q[0] = QS[C[0]] = 1
for i in range(1,N):
    if C[i] == C[i-1]:
        Q[i] = 0
    else:
        Q[i] = (P[i-1] + Q[i-1]) % M

    P[i] = QS[C[i]]
    QS[C[i]] = (QS[C[i]] + Q[i]) % M

print((P[N-1]+Q[N-1]) % M)