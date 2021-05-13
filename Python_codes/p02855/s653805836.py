h, w, k = map(int, input().split())
S = [list(input()) for i in range(h)]

ans = [[0 for i in range(w)] for j in range(h)]
cnt = 1
no_sb = ['.' for i in range(w)]
no_sb_row = []

for i in range(h):
    flag = True
    if S[i] == no_sb:
        no_sb_row.append(i)
    else:
        for j in range(w):
            if S[i][j] == '#' and flag:
                flag = False
            elif S[i][j] == '#':
                cnt += 1
            ans[i][j] = cnt
        cnt += 1

for row in no_sb_row:
    for i in range(row+1, h):
        if i not in no_sb_row:
            ans[row] = ans[i]
            break
    else:
        for j in range(row-1, -1, -1):
            if j not in no_sb_row:
                ans[row] = ans[j]
                break

for a in ans:
    print(*a)
