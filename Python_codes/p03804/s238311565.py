N,M = map(int, input().split())

A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        C = [A[k][i:i+M] for k in range(j, j+M)]
        if B == C:
            print('Yes')
            exit()

print('No')