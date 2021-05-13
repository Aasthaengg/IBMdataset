N = int(input())
sumMoney = 0
for _ in range(N):
    x, u = input().split()
    if u == "BTC":
        sumMoney += float(x) * 380000.0
    else:
        sumMoney += float(x)
print(sumMoney)
