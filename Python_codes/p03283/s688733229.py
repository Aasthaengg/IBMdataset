N, M, Q = map(int, input().split(' '))
count = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
    L, R = map(int, input().split(' '))
    count[L][R] += 1

for i in range(N + 1):
    for j in range(1, N + 1):
        count[i][j] += count[i][j - 1]

for i in range(1, N + 1):
    for j in range(N + 1):
        count[i][j] += count[i - 1][j]

for _ in range(Q):
    p, q = map(int, input().split(' '))
    ans = count[q][q] - count[q][p - 1] - count[p - 1][q] + count[p - 1][p - 1]
    print(ans)