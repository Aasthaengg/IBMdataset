N = int(input())

c = [[0] * 10 for _ in range(10)]
for i in range(1, N+1):
    i_first = int(str(i)[0])
    i_last = int(str(i)[-1])
    c[i_first][i_last] += 1

cnt = 0
for i in range(10):
    for j in range(10):
        cnt += c[i][j] * c[j][i]
print(cnt)