import math
n = int(input())
count = 0
for i in range(n):
    a = int(input())
    for j in range(2,int(math.sqrt(a) + 1)):
        if a % j == 0:
            break
    else:
        count += 1  
print(count)