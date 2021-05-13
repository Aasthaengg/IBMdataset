from collections import defaultdict
h, w, m = map(int, input().split())

row = [[0, 0] for _ in range(h + 1)]
col = [[0, 0] for _ in range(w + 1)]
ex = defaultdict(bool)
for i in range(m):
    r, c = map(int, input().split())
    row[r][0] += 1
    col[c][0] += 1
    row[r][1] = r
    col[c][1] = c
    ex[(r, c)] = True
row = sorted(row)[::-1]
col = sorted(col)[::-1]
ans = 0
for i in range(0, h + 1):
    for j in range(0, w + 1):
        ans = max(ans, row[i][0] + col[j][0] - ex[(row[i][1], col[j][1])])
        if not ex[(row[i][1], col[j][1])]:
            # iが同一だったら、jの値降順に見てるので木って良い
            break

print(ans)
