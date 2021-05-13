import math
X = int(input())

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

for i in range(10**7):
    if i < X:
        continue
    elif is_prime(i) is True:
        print(i)
        exit()
