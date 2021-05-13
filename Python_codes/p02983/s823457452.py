L, R = map(int, input().split())
ans = 2019
if R - L >= 2018:
    print(0)
else:
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            if i * j % 2019 < ans:
                ans = i * j % 2019
    print(ans)