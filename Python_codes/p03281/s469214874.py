import math
N = int(input())
count = 0
def divisoros_count(n):
    num = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            num += 1
            if n != i**2:
                num += 1
    return num

for i in range(1,N+1,2):
    if divisoros_count(i) == 8:
        count += 1

print(count)