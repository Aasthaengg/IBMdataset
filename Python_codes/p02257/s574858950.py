from math import sqrt


def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

result = 0
for i in range(int(input())):
    result += isprime(int(input()))
print(result)