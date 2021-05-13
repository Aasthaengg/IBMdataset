import math
n = int(input())

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

i = 0

while(True):
    if is_prime(n+i):
        print(n+i)
        exit()
    else:
        i += 1
