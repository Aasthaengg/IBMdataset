from math import sqrt

def isPrime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    i = 3
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 2

    return True


row_num = int(input())
count = 0
for row in range(row_num):
    if isPrime(int(input())):
        count += 1

print(count)

