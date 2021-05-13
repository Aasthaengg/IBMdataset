import math
a, b = map(int, input().split())

def is_prime(num):
    if num == 2:
        return True
    elif num <  3 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

if b > a:
    a, b = b, a
c = []
for i in range(1, int(math.sqrt(b))+1):
    if b%i == 0:
        k = b//i
        if a%k == 0:
            if is_prime(k):
                c.append(k)
        if a%i == 0:
            if is_prime(i):
                c.append(i)
print(len(set(c))+1)