n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(1, (n + 1)):
    like1 = a[i - 1]
    like2 = a[like1 - 1]
    if i == like2:
        ans += 1
print(ans // 2)
