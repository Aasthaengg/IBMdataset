L, R = map(int, open(0).read().split())

ans = 2020
m = min(L + 2020, R) + 1
for i in range(L, m):
    for j in range(i + 1, m):
    	ans = min(ans, i * j % 2019)

print(ans)
