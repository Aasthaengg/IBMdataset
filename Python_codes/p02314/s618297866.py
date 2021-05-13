INF = float('inf')
N, M = map(int, input().split())
C = [int(c) for c in input().split()]
T = [[INF] * (N + 1) for _ in range(M + 1)]
for i in range(M + 1):
    T[i][0] = 0

for i in range(1, M + 1):
        for j in range(1, N + 1):
            if N + 1 < j - C[i - 1] or j - C[i - 1] < 0:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(T[i - 1][j], T[i][j - C[i - 1]] + 1)

ans = []
for i in range(1, M + 1):
    ans.append(T[i][N])

print(min(ans))

