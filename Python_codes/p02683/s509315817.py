from itertools import combinations
N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
flug = True
for j in range(1, M + 1):
    sum_test = 0
    for i in range(N):
        sum_test += A[i][j]
    if sum_test < X:
        flug = False
        break
N_idx = [n for n in range(N)]
rec_tes = 0
for i in range(N):
    rec_tes += A[i][0] 
for i in range(N):
    for j in combinations(N_idx, r = i + 1):
        for k in range(1, M + 1):
            sum_und = 0
            sum_tes = 0
            for h in j:
                sum_und += A[h][k]
                sum_tes += A[h][0]
            if sum_und < X:
                break
        if sum_und >= X and sum_tes < rec_tes:
            rec_tes = sum_tes
if flug:
    print(rec_tes)
else:
    print(-1)