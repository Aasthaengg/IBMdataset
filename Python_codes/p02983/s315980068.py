l, r = map(int, input().split())
ans = 2019
if r - l + 1 >= 2019:
    ans = 0
else:
    for i in range(l, r + 1):
        for k in range(i + 1, r + 1):
            if ans > (i * k) % 2019:
                ans = (i * k) % 2019
            else:
                continue
print(ans)
