H, W, K = map(int, input().split())
fi = []
for _ in range(H):
    s = input()
    fi.append(s)
a = 2 ** H
b = 2 ** W
total = 0

for i in range(a * b):
    lh = list()
    lw = list()

    for j in range(H):
        if i & (1 << j):
            lh.append(1)
        else:
            lh.append(0)
    for j in range(W):
        if i & (1 << (j + H)):
            lw.append(1)
        else:
            lw.append(0)
    # print(lh)
    # print(lw)

    cnt = 0
    for j in range(H):
        for l in range(W):
            if lh[j] == 1 or lw[l] == 1:
                continue
            if fi[j][l] == '#':
                cnt += 1
    # print(cnt)
    if cnt == K:
        total += 1

print(total)
