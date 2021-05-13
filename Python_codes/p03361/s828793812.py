h, w = map(int, input().split())
a = [input() for _ in range(h)]
flag = True
def check(x, y):
    candidates = []
    if x > 0:
        candidates.append(a[x - 1][y])
    if x < h - 1:
        candidates.append(a[x + 1][y])
    if y > 0:
        candidates.append(a[x][y - 1])
    if y < w - 1:
        candidates.append(a[x][y + 1])
    if '#' in candidates:
        return True
    else:
        return False

for i in range(w):
    for j in range(h):
        if a[j][i] == '#':
            if check(j, i):
                pass
            else:
                flag = False
                break
print('Yes') if flag else print('No')