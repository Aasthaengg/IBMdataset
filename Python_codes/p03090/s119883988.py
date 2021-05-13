N = int(input())
M = (N * (N - 1)) // 2

ans_lst = [[1] * N for _ in range(N)]

if N % 2 == 0:
    for i in range(N):
        ans_lst[i][N - i - 1] = 0
else:
    for i in range(N - 1):
        ans_lst[i][N - i -2] = 0
#output
M = 0
for i in range(N):
    for j in range(i + 1, N):
        if ans_lst[i][j] == 1:
            M += 1

print (M)
for i in range(N):
    for j in range(i + 1, N):
        if ans_lst[i][j] == 1:
            print (i + 1, j + 1)