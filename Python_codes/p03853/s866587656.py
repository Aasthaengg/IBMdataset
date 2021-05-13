H, W = map(int, input().split())
C = [input() for _ in range(H)]
for i in range(1, 2 * H + 1):
    for j in range(1, W + 1):
        print(C[((i + 1) // 2) - 1][j - 1], end='')
    print()
