import math


def is_prime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i = i + 2

    return True


n = int(input())
numbers = [int(input()) for i in range(n)]


count = 0
for i in range(n):
    if is_prime(numbers[i]) is True:
        count += 1

print(count)

