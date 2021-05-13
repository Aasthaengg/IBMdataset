n, m, x = map(int, input().split())
a = [[] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
ans = 10000000000000
for i in range(2 ** n):
    money = 0
    understand = [0] * m
    for j in range(n):
        if i >> j & 1:
            money += a[j][0]
            for k in range(1, m + 1):
                understand[k - 1] += a[j][k]
    if min(understand) >= x:
        ans = min(money, ans)
print(ans if ans < 10000000000000 else -1)
