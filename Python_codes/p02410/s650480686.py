N, M = map(int, raw_input().split())

A = [[0 for j in range(M)]for i in range(N)]
B = [0 for j in range(M)]
C = [0 for i in range(N)]

# Input
for i in range(N):
    Ai = map(int, raw_input().split())
    for j in range(M):
        A[i][j] = Ai[j]

for j in range(M):
    B[j] = input()

# Calc
for i in range(N):
    for j in range(M):
        C[i] = C[i] + A[i][j]*B[j]

for i in range(N):
    print C[i]