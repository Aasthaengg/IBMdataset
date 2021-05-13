n, t = map(int, input().split())
a = list(map(int, input().split()))
max_value = [0] * n #a[i]以降の最大値
max_value[-1] = a[-1]
for i in range(-2, -n - 1, -1):
    max_value[i] = max(max_value[i + 1], a[i])
max_profit = 0
for i in range(n - 1):
    max_profit = max(max_profit, max_value[i] - a[i])
ans = 0
for i in range(n - 1):
    if max_value[i] - a[i] == max_profit: ans += 1
print(ans)