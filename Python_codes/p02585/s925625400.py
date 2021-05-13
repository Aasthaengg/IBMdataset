N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))

move_db = [[0] * N for _ in range(65)]
point_db = [[0] * N for _ in range(65)]
maxpoint_db = [[0] * N for _ in range(65)]

for i, (p, c) in enumerate(zip(P, C)):
    move_db[0][i] = p
    point_db[0][i] = c
    maxpoint_db[0][i] = c

for i in range(40):
    for j in range(N):
        move_db[i+1][j] = move_db[i][move_db[i][j]]
        point_db[i+1][j] = point_db[i][move_db[i][j]] + point_db[i][j]
        maxpoint_db[i+1][j] = max(maxpoint_db[i][j], point_db[i][j] + maxpoint_db[i][move_db[i][j]])

res = -10 ** 19
for i in range(N):
    tmp, now = 0, i
    for d in range(32):
        if K&(1<<d):
            res = max(res, tmp + maxpoint_db[d][now])
            tmp += point_db[d][now]
            now = move_db[d][now]

print(res)
