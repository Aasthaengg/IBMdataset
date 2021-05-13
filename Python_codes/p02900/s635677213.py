#4問目
import math
import fractions
import collections
A, B = map(int, input().split())

count = 0
gcd = fractions.gcd(A,B)

def devisor(num):
    array = []
    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if(num % i == 0):
            array.append(i)
            array.append(math.floor(num / i))
    return array

def prime(n):
    prime = []
    while n % 2 == 0:
        prime.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime.append(n)
    return prime

print(len(collections.Counter(prime(gcd))) + 1)