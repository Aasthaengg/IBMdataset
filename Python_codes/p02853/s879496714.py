#DDCC Finals
X, Y = map(int,input().split())
money = 0
moneyX = 400000 - X*100000
moneyY = 400000 - Y*100000
if moneyX > 0:
    money += moneyX
if moneyY > 0:
    money += moneyY
if money == 600000:
    money += 400000
print(money)