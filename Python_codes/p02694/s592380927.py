X = int(input())
i = 0
money = 100
r = 101
while money < X:
    money *= r
    money //= 100
    i += 1
print(i)
