n = int(input())
s = input()

ans = 0
for i in range(1, n):
    x = s[0:i]
    y = s[i:]

    uniq_x = set(x)
    uniq_y = set(y)

    cnt = 0
    for c in uniq_y:
        if c in uniq_x:
            cnt += 1

    ans = max(ans, cnt)

print(ans)
