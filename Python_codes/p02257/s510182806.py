# coding:utf-8
import math
def isprime(x):
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
n = input()
array = []
cnt = 0
for i in range(n):
    array.append(input())
for i in range(n):
    if isprime(array[i]):
        cnt += 1
print cnt