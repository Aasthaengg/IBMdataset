H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
A = [['#' for i in range(W)] for j in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            a = 0
            if i > 0 and j > 0:
                if S[i - 1][j - 1] == '#':
                    a += 1
            if i > 0:
                if S[i - 1][j] == '#':
                    a += 1
            if i > 0 and j < W - 1:
                if S[i - 1][j + 1] == '#':
                    a += 1
            if j > 0:
                if S[i][j - 1] == '#':
                    a += 1
            if j < W - 1:
                if S[i][j + 1] == '#':
                    a += 1
            if i < H - 1 and j > 0:
                if S[i + 1][j - 1] == '#':
                    a += 1
            if i < H - 1:
                if S[i + 1][j] == '#':
                    a += 1
            if i < H - 1 and j < W - 1:
                if S[i + 1][j + 1] == '#':
                    a += 1
            A[i][j] = a
for i in range(H):
    ans = [str(a) for a in A[i]]
    ans = ''.join(ans)
    print(ans)