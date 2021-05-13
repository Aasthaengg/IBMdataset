h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
r = [[0]*w for _ in range(h)]
for i in range(h):
    flg = False
    for j in range(w):
        if s[i][j]=='.':
            if not flg:
                tmp = 0
                begin = j
                flg = True
            tmp += 1
        if flg and s[i][j]=='#':
            for k in range(begin, j):
                r[i][k] = tmp
            flg = False
    if flg:
        for k in range(begin, w):
            r[i][k] = tmp
c = [[0]*w for _ in range(h)]
for i in range(w):
    flg = False
    for j in range(h):
        if s[j][i]=='.':
            if not flg:
                tmp = 0
                begin = j
                flg = True
            tmp += 1
        if flg and s[j][i]=='#':
            for k in range(begin, j):
                c[k][i] = tmp
            flg = False
    if flg:
        for k in range(begin, h):
            c[k][i] = tmp
ans = 0
for row1, row2 in zip(r, c):
    for e1, e2 in zip(row1, row2):
        if ans<e1+e2-1:
            ans = e1+e2-1
print(ans)