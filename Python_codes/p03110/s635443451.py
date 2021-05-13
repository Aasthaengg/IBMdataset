n = int(input())
gifts = []
for i in range(n):
    gift = input().split()
    gifts.append(gift)
ans = 0
for j in range(n):
    if gifts[j][1] == "BTC":
        price = float(gifts[j][0]) * 380000
        ans += price
    elif gifts[j][1] == "JPY":
        price = float(gifts[j][0])
        ans += price
print(ans)