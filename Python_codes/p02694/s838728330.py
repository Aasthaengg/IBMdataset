X = int(input())
money = 100
for i in range(1, 100000):
    money = money + (money // 100)
    if money >= X:
        print(i)
        break
