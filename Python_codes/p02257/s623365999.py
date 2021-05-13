N = int(input())
n = [int(input()) for i in range(N)]

def Is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i < int(n ** (0.5))+ 1:
        if n % i == 0:
            return False
        i += 2
    return True

count = 0
for j in n:
    if Is_prime(j):
        count += 1

print (count)