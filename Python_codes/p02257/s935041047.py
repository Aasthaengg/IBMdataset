from math import sqrt
def isPrime(n):
    if n == 2:
        return 1
    if n == 1 or n % 2 == 0:
        return 0
    for i in range(3,int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

from sys import stdin
print(sum([isPrime(int(n))for n in stdin]))