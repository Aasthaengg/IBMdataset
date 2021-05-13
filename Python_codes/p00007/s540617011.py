money = 100000
unit = 1000
user = input()
n = int(user)
for i in range(n):
    money *= 1.05
    if money % unit != 0:
        money -= money % unit
        money += unit
print(str(int(money)))