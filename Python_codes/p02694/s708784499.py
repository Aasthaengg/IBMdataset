import sys

X = int(input())

i = 0
money = 100

while True:
    i += 1
    money += money//100
    if X <= money:
        print(i)
        sys.exit()