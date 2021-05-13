import math
def prime_number(num):
    if num == 1 :
        return 0
    for i in range(2,int(math.sqrt(num))+1):
        if (num % i) == 0:
            return 0
    return 1

N =int(input())
count = 0
for i in range(0,N):
    num = int(input())
    count += int(prime_number(num))
print(count)
