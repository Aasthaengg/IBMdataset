h, w = map(int, input().split())

mtx = [input() for _ in range(h)]

ret_mtx1 = [[0] * w for _ in range(h)]
ret_mtx2 = [[0] * w for _ in range(h)]
ret_mtx3 = [[0] * w for _ in range(h)]
ret_mtx4 = [[0] * w for _ in range(h)]

# left 2 right
for i in range(h):
    for j in range(w):
        if mtx[i][j] == '.':
            ret_mtx1[i][j] = 1 if i == 0 else ret_mtx1[i-1][j] + 1
            ret_mtx2[i][j] = 1 if j == 0 else ret_mtx2[i][j-1] + 1
        if mtx[-1-i][-1-j] == '.':
            ret_mtx3[-1-i][-1-j] = 1 if i == 0 else ret_mtx3[-i][-1-j] + 1
            ret_mtx4[-1-i][-1-j] = 1 if j == 0 else ret_mtx4[-1-i][-j] + 1

ret = 0

for i in range(h):
    for j in range(w):
        tmp = ret_mtx1[i][j] + ret_mtx2[i][j] + \
            ret_mtx3[i][j] + ret_mtx4[i][j] - 3
        ret = max(ret, tmp)

print(ret)
