import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

x = inint()

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.floor(math.sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True


for i in range(1,10**6):
    bool = isPrime(i)
    if bool and i >= x:
        print(i)
        break
