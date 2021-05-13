from math import sqrt, ceil
X = int(input())

def isprime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for j in range(3, ceil(sqrt(x))+1, 2):
        if x % j == 0:
            return False
    return True

for i in range(10**9):
    if isprime(X+i):
        print(X+i)
        break
