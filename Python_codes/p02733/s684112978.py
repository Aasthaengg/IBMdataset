h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
res = 1000000
for i in range(2 ** (h - 1)):
    l = [0]
    cnt = 0
    for j in range(h - 1):
        if (i >> j) & 1:
            l.append(j + 1)
            cnt += 1
    l.append(h)
    li = [0] * (cnt + 1)
    j = 0
    ans = cnt
    f = 0
    while j < w:
        sm = 0
        idx = 0
        for i in range(h):
            if l[idx + 1] <= i:
                if sm > k:
                    f = 1
                    break
                sm = 0
                if li[idx] > k:
                    ans += 1
                    break
                idx += 1
            if s[i][j] == '1':
                sm += 1
                li[idx] += 1
        else:
            if li[idx] > k:
                if sm > k:
                    f = 1
                    break
                ans += 1
                li = [0] * (cnt + 1)
                continue
            j += 1
            continue
        if f:
            break
        li = [0] * (cnt + 1)
    if not f:
        res = min(res, ans)
print(res)
