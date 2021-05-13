h, w, k = map(int, input().split())
s = [None] * h
st = [0] * h
ans = [[0] * w for _ in range(h)]
cnt = 0
for i in range(h):
    s[i]  = list(input())
    st[i] = s[i].count('#')
col_first = False
col_first_num = 0
for i in range(h):
    if st[i] == 0:
        if col_first:
            for j in range(w):
                ans[i][j] = ans[i-1][j]
    else:
        cnt += 1
        if not col_first:
            col_first_num = i
        col_first = True
        row_first = False
        for j in range(w):
            if row_first:
                if s[i][j] == '#':
                    cnt += 1
                ans[i][j] = cnt
            else:
                if s[i][j] == '#':
                    row_first = True
                ans[i][j] = cnt
for i in range(h):
    if ans[i][0] == 0:
        for j in range(w):
            ans[i][j] = ans[col_first_num][j]
    else:
        break
for i in ans:
    for j in i:
        print(j, end=' ')
    print()