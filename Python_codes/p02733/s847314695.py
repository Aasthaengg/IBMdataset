h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
ans = float("inf")
for bit in range(1 << (h - 1)):
    cnt = 0
    l = [0] * h
    for i in range(h - 1):
        if bit & (1 << i):
            cnt += 1
        l[i + 1] = cnt
    m = max(l) + 1
    cnt2 = m - 1
    c = [0] * m
    for j in range(w):
        cur = [0] * m
        for i in range(h):
            c[l[i]] += int(s[i][j])
            cur[l[i]] += int(s[i][j])
            if c[l[i]] > k:
                cnt2 += 1
                for i in range(m):
                    c[i] = cur[i]
    ans = min(ans, cnt2)
print(ans)