import math

def is_prime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i = i + 1
    return True

N = int(input())
cnt = 0
for i in range(0, N):
    n = int(input())
    if (is_prime(n)):
        cnt = cnt + 1
        
print(cnt)