h, w = map(int, input().split())
fld = [list(map(int, input().split())) for _ in range(h)]


def generate_unagi():
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                yield (i, j)
        else:
            for j in reversed(range(w)):
                yield (i, j)


ans = []
it = list(generate_unagi())
for (i, j), (i2, j2) in zip(it, it[1:]):
    if fld[i][j] % 2 == 0:
        continue
    fld[i][j] -= 1
    fld[i2][j2] += 1
    ans.append((i+1, j+1, i2+1, j2+1))

print(len(ans))
for row in ans:
    print(*row)