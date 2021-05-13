h, w, k = map(int, input().split())
cakes = []
for _ in range(h):
    row = list(input())
    cakes.append(row)

# 左から埋める
c = 1
for i in range(h):
    for j in range(w):
        if cakes[i][j] == '#':
            cakes[i][j] = c
            for k in range(0, j):
                if cakes[i][k] == '.':
                    cakes[i][k] = c
            c += 1

# 右側に残っているモノを、一番左のモノで埋める。
for i in range(h):
    for j in range(w):
        if cakes[i][j] == '.':
            cakes[i][j] = cakes[i][j - 1]

#上下を埋める
for i in range(1, h):
    for j in range(w):
        if cakes[i][j] == '.':
            cakes[i][j] = cakes[i - 1][j]
for i in range(h - 1)[::-1]:
    for j in range(w):
        if cakes[i][j] == '.':
            cakes[i][j] = cakes[i + 1][j]

for r in cakes:
    print(*r)