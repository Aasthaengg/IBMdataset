h, w, k = map(int, input().split())
SS = [list(input()) for _ in range(h)]
num = 1
ans = [[0] * w for _ in range(h)]

for i in range(h):
    S = SS[i]

    if S != ['.'] * w:
        for j in range(w):
            s = S[j]
            if s == '#':
                ans[i][j] = num
                if j != w - 1:
                    if '#' in S[j + 1:]:
                        num += 1
            else:
                ans[i][j] = num
        num += 1

cnt = 1

for num, a in enumerate(ans):
    if a == [0] * w:
        cnt += 1
        continue
    else:
        for i in range(cnt):
            a = list(map(str, a))
            print(' '.join(a))
        cnt = 1

cnt1 = 0
if cnt != 1:
    p = []
    ans = ans[::-1]
    for i in range(h):
        b = ans[i]
        if b == [0] * w:
            cnt1 += 1
        else:
            for j in range(cnt1):
                b = list(map(str, b))
                print(' '.join(b))
            exit()


