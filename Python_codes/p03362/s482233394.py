import sys
input = sys.stdin.readline

n = int(input())
prime = []
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
for i in range(2, 55556):
    if is_prime(i) and i % 5 == 1:
        prime.append(i)
print(*prime[:n])