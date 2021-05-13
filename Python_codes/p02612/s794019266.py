money1 = int(input())
if money1 % 1000 != 0:
    money2 = 1000 - (money1 % 1000)
    print(str(money2))
else:
    money2 = 0
    print(str(money2))