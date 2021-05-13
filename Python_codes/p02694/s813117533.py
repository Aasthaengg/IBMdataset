X = int(input())

time = 0
money = 100
while True:
    time += 1
    money += money // 100
    if money >= X:
        print(time)
        break