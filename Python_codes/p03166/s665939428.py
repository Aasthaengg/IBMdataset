import sys
input = sys.stdin.readline

n, m = map(int,input().split())
C = [list(map(int,input().split())) for i in range(m)]
for i in range(m):
    for j in range(2):
        C[i][j] -= 1

D = [0] * n
M = [[] for i in range(n)]
for i in range(m):
    M[C[i][0]].append(C[i][1])

IN = [0] * n
for i in range(m):
    IN[C[i][1]] += 1

S = []
s = 0

for i in range(n):
    if IN[i] == 0:
        S.append(i)

while s < len(S):
    for x in M[S[s]]:
        IN[x] -= 1
        if IN[x] == 0:
            S.append(x)
    s += 1



for i in range(n):
    for j in range(len(M[S[i]])):
        D[M[S[i]][j]] = max(D[M[S[i]][j]], D[S[i]] + 1)
print(max(D))