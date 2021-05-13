h, w, k = map(int, input().split())
c = list(input() for _ in range(h))
# print(c)

cnt = 0

for rows in range(1 << h):
    for cols in range(1 << w):
        black = 0
        for i in range(h):
            if (rows >> i) % 2 == 1:
                continue
            for j in range(w):
                if (cols >> j) % 2 == 1:
                    continue
                black += c[i][j] == '#'
        if black == k:
            cnt += 1

print(cnt)