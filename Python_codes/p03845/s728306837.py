N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [list(map(int, input().split())) for i in range(M)]
# P[i][0] = P_(i + 1), P[i][1] = X_(i + 1) となる
# 例：　P[0][1] = P_1, P[2][1] = X_3

for i in range(M):
    updated_T = T[:]
    updated_T[P[i][0] - 1] = P[i][1]

    print(sum(updated_T))
