import math
import sys

def is_prime(x):
    if x == 1: return 0
    elif x == 2: return 1
    elif x % 2 == 0: return 0

    n = 3
    while n <= math.sqrt(x):
        if x % n == 0:
            return 0
        n += 2
    return 1

n = int(raw_input())
count = 0
for i in range(n):
    x = int(raw_input())
    count += is_prime(x)

print count
