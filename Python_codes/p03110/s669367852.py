n = int(input())
ans = 0
for i in range(n):
    x,v = input().split()
    if v == "JPY":
        ans += int(x)
    elif v == "BTC":
        ans += float(x)*380000.0
print(ans)