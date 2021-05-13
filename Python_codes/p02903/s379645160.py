# https://atcoder.jp/contests/agc038/tasks/agc038_a

h, w, a, b = map(int, input().split())

matrix = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if (i < b) ^ (j < a):
            matrix[i][j] = 1

for r in matrix:
    print(''.join(map(str, r)))
