import sys

N, M = map(int, input().split())
shop = []
count = 0
money = 0
for i in range(N):
    a, b = map(int, input().split())
    shop.append([a, b])

shop = list(sorted(shop))

for i in range(N):
    buy = min(M, shop[i][1])
    money += buy * shop[i][0]
    M = M - buy
    if M == 0:
        print(money)
        sys.exit()