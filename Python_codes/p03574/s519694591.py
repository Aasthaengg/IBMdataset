H, W = map(int, input().split())
S = [list(map(str, input())) for _ in range(H)]

M = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            for k in range(3):
                for l in range(3):
                    if k == l == 1:
                        M[i + k][j + l] = '#'
                    else:
                        if M[i + k][j + l] != '#':
                            M[i + k][j + l] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        print(M[i][j], end='')
    print('')