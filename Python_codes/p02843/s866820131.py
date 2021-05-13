x = int(input())
n = x // 100
x %= 100

for i in range(n):
    if x - 5 >= 0:
        x -= 5
    elif x - 4 >= 0:
        x -= 4
    elif x - 3 >= 0:
        x -= 3
    elif x - 2 >= 0:
        x -= 2
    elif x - 1 >= 0:
        x -= 1
    else:
        break

if x == 0:
    print(1)
else:
    print(0)