h,w,k = map(int,input().split())
S = [input() for _ in range(h)]
ans = [[0]*w for _ in range(h)]
flag = ['#' in S[i] for i in range(h)]
upcnt = 0
last = 0
now = 0
for i in range(h):
    if flag[i]:
        for j in range(w):
            if S[i][j] == '#':
                now += 1
                if last == 0:
                    for l in range(j):
                        ans[i][l] = now
                        if upcnt >= 1:
                            for m in range(i):
                                ans[m][l] = now
                    last = 1
            ans[i][j] = now
            if upcnt >= 1:
                for m in range(i):
                    ans[m][j] = now
            # if S[i][j] == '#':
                # now += 1
        upcnt = -1
        last = 0
    elif upcnt >= 0:
        upcnt += 1
    else:
        for j in range(w):
            ans[i][j] = ans[i-1][j]
for i in range(h):
    print(' '.join(str(i) for i in ans[i]))
