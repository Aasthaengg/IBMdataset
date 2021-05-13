import math

def isprime(z):
    if z == 2:
        return True
    
    if z < 2 or z % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(z):
        if z % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    n = int(input())
    c = 0
    for _ in range(n):
        if isprime(int(input())):
            c += 1
    print (c)
