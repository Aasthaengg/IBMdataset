MOD = 10 ** 9 + 7

n, k = map(int, input().split())
alst = list(map(int, input().split()))
ans = 0
loop1 = k * (k - 1) // 2
loop2 = (k + 1) * k // 2
loop1 %= MOD
loop2 %= MOD

for i, num in enumerate(alst):
    for j, num2 in enumerate(alst):
        if num > num2:
            if i < j:
                ans += loop2
                ans %= MOD
            else:
                ans += loop1
                ans %= MOD
print(ans)