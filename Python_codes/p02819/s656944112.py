import math

X = int(input())

def prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    m = math.floor(num/2) + 1
    for p in range(3, m, 2):
        if num % p == 0:
            return False
    return True

while prime(X) == False:
    X += 1

print(X)