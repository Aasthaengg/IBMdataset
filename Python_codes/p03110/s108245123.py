n = int(input())
ans = 0
for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == "JPY":
        ans += x
    elif u == "BTC":
        ans += x * 380000
print(ans)
