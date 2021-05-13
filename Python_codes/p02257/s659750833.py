from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

def isprime(x):
    if x==2:
        return True
    if x < 2 or x%2==0:
        return False
    i=3
    while True:
        if i > math.sqrt(x):
            break
        if x % i ==0:
            return False
        i += 2
    return True

try_num=int(input())
num_prime=0
for i in range(try_num):
    test_num=int(input())
    if isprime(test_num):
        num_prime += 1

print("%d"%(num_prime))

