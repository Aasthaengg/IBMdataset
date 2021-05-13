import math

X = int(input())

for i in range(X, 10**6):
    if i == 1:
        continue
    elif i == 2 or i == 3:
        print(i)
        break
    elif i % 2 == 0 or i % 3 == 0:
        continue
    for j in range(5, math.floor(math.sqrt(i)) + 1, 6):
        if i % j == 0 or i % (j+2) == 0:
            break
    else:
        print(i)
        break