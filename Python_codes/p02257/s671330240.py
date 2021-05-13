from math import sqrt
def prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        i = 3
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i += 2
    return True

n = int(input())
c = 0
for i in range(n):
    if(prime(int(input()))):
        c += 1

print(c)