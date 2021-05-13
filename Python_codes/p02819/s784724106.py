import math
x = int(input())

while True:
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            x += 1
            break
    else:
        break
print(x)
