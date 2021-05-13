def nxt(y, x, h, w):
    if y % 2 == 0:
        if x < w - 1:
            yn, xn = y, x + 1
        else:
            yn, xn = y + 1, w - 1
    else:
        if x > 0:
            yn, xn = y, x - 1
        else:
            yn, xn = y + 1, 0
    return yn, xn


h, w = map(int, input().split())
a = []

for i in range(h):
    line = list(map(int, input().split()))
    a.append(line)

ret = []

for i in range(h * w - 1):
    y = i // w
    if y % 2 == 0:
        x = i % w
    else:
        x = w - 1 - (i % w)
    if a[y][x] % 2 != 0:
        yn, xn = nxt(y, x, h, w)
        ret.append((y+1, x+1, yn+1, xn+1))
        a[yn][xn] += 1

print(len(ret))
for item in ret:
    print(' '.join(map(str, item)))
