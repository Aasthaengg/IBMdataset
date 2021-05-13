import math
def isPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.ceil(x**0.5))+1):
        if x % i == 0:
            return False
    return True

n = input()
l = [input() for i in range(n)]
count = 0
for i in l:
    if isPrime(i):
        count += 1
print count