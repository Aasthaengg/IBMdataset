def abc127d():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for item in a:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    for _ in range(m):
        b, c = map(int, input().split())
        if c in d:
            d[c] += b
        else:
            d[c] = b
    cnt = n
    ans = 0
    for k in sorted(d.keys(), reverse=True):
        v = min(cnt, d[k])
        ans += k * v
        cnt -= v
    print(ans)
abc127d()