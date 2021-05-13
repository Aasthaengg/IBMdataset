N, C = map(int, input().split())
R = [[0, 0]]
L = [[0, 0]]
R_half = -1
for i in range(N):
    x, v = map(int, input().split())
    R.append([x, v])
for i in R[::-1]:
    L.append([C - i[0], i[1]])
L.pop(-1)

R_sum = [0]
L_sum = [0]
R_sum2 = [0]
L_sum2 = [0]
total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0
for i in range(1, N + 1):
    total_1 += R[i][1] - (R[i][0] - R[i-1][0])
    total_2 += L[i][1] - (L[i][0] - L[i-1][0])
    total_3 += R[i][1] - 2*(R[i][0] - R[i-1][0])
    total_4 += L[i][1] - 2*(L[i][0] - L[i-1][0])
    R_sum.append(total_1)
    L_sum.append(total_2)
    R_sum2.append(total_3)
    L_sum2.append(total_4)
result_1 = max(R_sum)
result_2 = max(L_sum)
big_R = []
big_L = []
t = 0
p = 0
for i in range(N+1):
    t = max(t, R_sum[i])
    big_R.append(t)
    p = max(p, L_sum[i])
    big_L.append(p)
result_3 = 0
result_4 = 0
for i in range(N+1):
    result_3 = max(result_3, L_sum2[i] + big_R[N - i])
    result_4 = max(result_4, R_sum2[i] + big_L[N - i])
print(max([result_1, result_2, result_3, result_4]))