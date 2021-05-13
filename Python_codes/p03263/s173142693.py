h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
func=[]
for i in range(h):
    for j in range(w):
        if a[i][j] & 1:
            if j < w - 1:
                a[i][j + 1] += 1
                a[i][j] -= 1
                func.append((i, j, i, j + 1))

            elif i < h - 1:
                a[i + 1][j] += 1
                a[i][j] -= 1
                func.append((i, j, i + 1, j))

# for i in a:
#     print(*i)
print(len(func))
for y, x, i, j in func:
    print(y + 1, x + 1, i + 1, j + 1)
