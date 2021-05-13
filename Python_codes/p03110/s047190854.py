N = int(input())
money = [input().split() for i in range(N)]

JPY = [int(money[i][0]) for i in range(N) if money[i][1] == 'JPY']
BTC = [float(money[i][0]) * 380000 for i in range(N) if money[i][1] == 'BTC']

print(sum(JPY) + sum(BTC))