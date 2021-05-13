n = int(input())
a = list(map(int, input().split()))
tot = sum(a) // 2
ans = [-1] * n
now = sum(a[:n - 1:2])
i = 0
j = n - 1
while ans[j] == -1:
    ans[j] = tot - now
    now += a[j] - a[i]
    j = (j + 2) % n
    i = (i + 2) % n
print(*map(lambda x: 2 * x, ans))
