import math
def isPrime(n):
    if n <= 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        i = 5
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            if n % (i + 2) == 0:
                return False
            i+=6
    return True
            
N = int(raw_input())
D = [int(raw_input()) for i in xrange(N)]
count = 0
for i in D:
    if isPrime(i) == True:
        count += 1
print count