h,w,k = map(int,input().split())
s = [input() for _ in range(h)]
row = []
col = []

flagr = flagc = flags = False
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if flagc:
                col.append(j)
            else:
                flagc = True
            flags = True
    if flags:
        col.append(w)
        if flagr:
            row.append(i)
        else:
            flagr = True
        flagc = flags = False
row.append(h)

ans = [["" for _ in range(w)] for _ in range(h)]
cnt = 1
idx = 0
sr = sc = 0
for er in row:
    while sc != w:
        ec = col[idx]
        for i in range(sr,er):
            for j in range(sc,ec):
                ans[i][j] = str(cnt)
        cnt += 1
        idx += 1
        sc = ec
    sc = 0
    sr = er

for i in range(h): print(" ".join(ans[i]))