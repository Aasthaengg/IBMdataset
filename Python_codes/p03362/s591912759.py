import math


def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    return True


def callIsPrime(input_num=1000):
    numbers = []
    for i in range(1, input_num):
        if isPrime(i):
            numbers.append(i)

    return numbers


n = int(input())
pms = callIsPrime(55555)

ret = []

for item in pms:
    if item % 5 == 1:
        ret.append(item)

print(" ".join(map(str, ret[:n])))
