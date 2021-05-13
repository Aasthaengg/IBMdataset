# -*- coding: utf-8 -*-

def isPrime(p):
    if p == 2:
        return True
    elif p < 2 or p%2 == 0:
        return False
    elif pow(2, p-1, p) == 1:
        return True
    else:
        return False

n = int(raw_input())
count = 0
for i in range(n):
    if isPrime(int(raw_input())):
        count += 1
print count