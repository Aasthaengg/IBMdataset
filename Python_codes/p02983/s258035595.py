L, R = map(int, input().split())
res = [0] * 2019
for i in range(L, R + 1):
    if res[i % 2019] > 0:
        break
    else:
        res[i % 2019] += 1

if res[0] == 1:
    print(0)
else:
    ans = 2019
    for i in range(2019):
        for j in range(i + 1, 2019):
            if res[i] == res[j] == 1:
                ans = min(ans, i * j % 2019)
    print(ans)