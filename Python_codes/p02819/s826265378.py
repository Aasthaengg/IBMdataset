import math
a = int(input())
b = int(math.sqrt(a)) +1

for k in range(200000):
    count = 0
    for i in range(2,b):
        if (a+k) % i == 0:
            count +=1
    if count == 0:
        print(a+k)
        break