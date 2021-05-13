L, R = map(int, input().split())
if R - L >= 2019:
    ans = 0
else:
    ans = 2018
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            a = (i * j) % 2019
            if ans > a:
                ans = a
            if ans == 1:
                break
print(ans)