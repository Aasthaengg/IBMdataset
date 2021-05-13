from collections import defaultdict

M = 10**9 + 7
N = int(input())
C = [0]*N
for i in range(N):
    C[i] = int(input())

class increment:
    def __init__(self, start=0):
        self.index = start-1

    def __call__(self):
        self.index += 1
        return self.index

ui = defaultdict(increment())
clists = []
Nc = 0
for i in range(N):
    n = ui[C[i]]
    if n >= Nc:
        clists.append([i])
        Nc += 1
    else:
        clists[n].append(i)

P = [0]*N
Q = [0]*N
Q[0] = 1
QS = [0]*Nc
QS[ui[C[0]]] = 1
for i in range(1,N):
    if C[i] == C[i-1]:
        Q[i] = 0
    else:
        Q[i] = (P[i-1] + Q[i-1]) % M
    
    cind = ui[C[i]]
    P[i] = QS[cind]
    QS[cind] = (QS[cind] + Q[i]) % M

print((P[N-1]+Q[N-1]) % M)