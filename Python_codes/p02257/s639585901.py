import math
n = input()
c = 0


for i in range(int(n)):
    x = int(input())
    if x == 1:
        x = 0
    for j in range(2,math.floor(math.sqrt(float(x)))+ 1):
        if x % j == 0:
            x = 0
            break
    if x != 0:
        c += 1	
print(c)