n, t = map(int, input().split())
a = list(map(int, input().split()))
INF = 10 ** 9 + 1

profit = [0] * n
buy_mn = INF
for i, e in enumerate(a):
    profit[i] = e - buy_mn
    buy_mn = min(buy_mn, e)

profit_mx = max(profit)
ans = profit.count(profit_mx)
print(ans)
