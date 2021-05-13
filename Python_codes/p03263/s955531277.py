def resolve():
    H, W = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(H)]
    ops = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                continue
            if j == W-1:
                if i == H-1:
                    continue
                else:
                    A[i][j] -= 1
                    A[i+1][j] += 1
                    ops.append([i+1, j+1, i+2, j+1])
            else:
                A[i][j] -= 1
                A[i][j+1] += 1
                ops.append([i+1, j+1, i+1, j+2])
    print(len(ops))
    [print(" ".join(map(str, op))) for op in ops]


if '__main__' == __name__:
    resolve()