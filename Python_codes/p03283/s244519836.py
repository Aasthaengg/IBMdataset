N, M, Q = map(int, input().split())
train = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    train[L][R] += 1
# print(train)

cumsum = [[0 for _ in range(N + 1)]for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        cumsum[i][j] = cumsum[i][j - 1] + train[i][j]
# print(cumsum)

for _ in range(Q):
    p, q = map(int, input().split())
    tmp = 0
    for i in range(p, q + 1):
        tmp += cumsum[i][q] - cumsum[i][p - 1]
    print(tmp)
