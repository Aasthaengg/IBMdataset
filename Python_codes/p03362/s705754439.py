import sys
input = sys.stdin.readline

n = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a = []

for i in range(2, 55556):
    if is_prime(i) and i % 5 == 1:
        a.append(i)

print(*a[:n])