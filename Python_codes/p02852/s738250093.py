n, m = map(int, input().split())
s = [0] * (n+1)
cnt = 0
for i, x in enumerate(input()):
    if x == "1":
        cnt += 1
        if cnt >= m: print(-1); exit()
        s[i] = 1
    else: cnt = 0

c = n
res = []

while True:
    nc = c - m
    if nc <= 0:
        res.append(c)
        break
    while s[nc]: nc += 1
    res.append(c - nc)
    c = nc

print(*reversed(res))