x, y = map(int, input().split())
ans = 10 ** 10
for i in range(2):
    for j in range(2):
        a = x
        b = y
        cnt = 0
        if i == 1:
            a *= -1
            cnt = 1
        if j == 1:
            b *= -1
            cnt += 1
        if a > b:
            continue
        cnt += b - a
        a += b - a
        #print(cnt, a, b)
        if a == b:
            ans = min(ans, cnt)

print(ans)
