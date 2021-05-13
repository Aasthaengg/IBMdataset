h, w, k = list(map(int, input().split()))
m = []

for i in range(h):
    m.append(input())

def count(h, w):
    cnt = 0
    for i in h:
        for j in w:
            if m[i][j] == '#': cnt += 1
    return cnt

def remove(l, x):
    return [y for y in l if y is not x]

def search(hs, ws, hmin, wmin):
    nblack = count(hs, ws)
    if nblack < k:
        return 0

    res = 0
    if wmin == 0:
        for i in range(hmin, h):
            hs_ = remove(hs, i)
            res += search(hs_, ws, i + 1, wmin)

    for j in range(wmin, w):
        ws_ = remove(ws, j)
        res += search(hs, ws_, hmin, j + 1)

    if nblack == k:
        return res + 1
    return res

x = search(list(range(h)), list(range(w)), 0, 0)
print(x)