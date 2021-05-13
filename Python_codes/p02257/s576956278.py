import math
n = int(input())

A = [0] * n
for i in range(n):
    A[i] = int(input())

# Naive method
def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
    return True

print(len([x for x in A if is_prime(x)]))