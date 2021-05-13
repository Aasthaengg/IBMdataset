# B - Minesweeper
import copy
H, W = map(int, input().split())
S_src = []
for i in range(H):
    S_src.append(list(input()))

S_tgt = copy.deepcopy(S_src)
for i in range(H):
    for j in range(W):
        if S_src[i][j] == '#':
            continue

        count = 0
        for m in range(-1, 2):
            if not (0 <= i + m < H):
                continue
            for n in range(-1, 2):
                if not (0 <= j + n < W):
                    continue
                if S_src[i+m][j+n] == '#':
                    count += 1
        S_tgt[i][j] = str(count)

for i in range(H):
    print("".join(S_tgt[i]))

