# -*- coding: utf-8 -*-

import sys

def isprime(n):
    for i in xrange(2, int(n ** 0.5)+1 ):
        if n % i == 0: return False
    return True


outList = []
for line in sys.stdin.readlines():
    List = map(int, line.strip().split())

    [a, b] = List

    # LCM
    LCM = 1
    i = 1
    while( i <= min(a, b) ):
        i += 1
        if not isprime(i): continue
        while(a % i == 0 and b % i == 0):
            LCM *= i
            a /= i
            b /= i

    # GCD
    GCD = List[0] * b

    print LCM, GCD