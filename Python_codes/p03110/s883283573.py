N = int(input())
K = 380000
ans = 0
import decimal
for _ in range(N):
    x, u = input().split()
    if u == "BTC":
        ans += K * decimal.Decimal(x)
    else:
        ans += int(x)
print(ans)