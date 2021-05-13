n, m = map(int, input().split())
sl = []
for i in range(m):
    s = list(map(int, input().split()))
    del s[0]
    sl.append(s)
p = list(map(int, input().split()))

ans = 0
for i in range(1 << n):
    ok = True
    for j in range(m):
        cnt = 0
        for k in range(len(sl[j])):
            if (i >> sl[j][k] - 1)%2 == 0:
                cnt += 1
        if cnt%2 != p[j]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)