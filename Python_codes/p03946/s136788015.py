n, t = map(int, input().split())
a = list(map(int, input().split()))

profit = [0] * n
buy_mn = a[0]
for i, e in enumerate(a[1:], 1):
    profit[i] = e - buy_mn
    buy_mn = min(buy_mn, e)

profit_mx = max(profit)
ans = profit.count(profit_mx)
print(ans)
