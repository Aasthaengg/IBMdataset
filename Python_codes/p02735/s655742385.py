H, W = map(int, input().split())
data = [list(map(str, input())) for _ in range(H)]


def g(m):
    if data[0][0] == '.':
        a = 0
    else:
        a = 1

    for i in range(1, m, 1):
        if data[0][i] == '.':
            continue
        elif data[0][i] == '#' and data[0][i - 1] == '.':
            a += 1
        else:
            continue
    return a


def h(n):
    if data[0][0] == '.':
        a = 0
    else:
        a = 1

    for i in range(1, n, 1):
        if data[i][0] == '.':
            continue
        elif data[i][0] == '#' and data[i - 1][0] == '.':
            a += 1
        else:
            continue
    return a

A = [0] + [g(i) for i in range(1,W+1)]
B = [0] + [h(i) for i in range(1,H+1)]
C = [[0]*(W+1) for i in range(H+1)]

for n in range(1,H+1):
    for m in range(1,W+1):
        if n == 1:
            C[n][m] = A[m]
        elif m == 1:
            C[n][m] = B[n]
        else:
            if data[n - 1][m - 1] == '.':
                C[n][m] = min(C[n - 1][m], C[n][m - 1])
            elif data[n - 2][m - 1] == '.':
                if data[n - 1][m - 2] == '.':
                    C[n][m] = min(C[n - 1][m] + 1, C[n][m - 1] + 1)
                else:
                    C[n][m] =  min(C[n - 1][m] + 1, C[n][m - 1])
            else:
                if data[n - 1][m - 2] == '.':
                    C[n][m] = min(C[n - 1][m], C[n][m - 1] + 1)
                else:
                    C[n][m] = min(C[n - 1][m], C[n][m - 1])


print(C[H][W])