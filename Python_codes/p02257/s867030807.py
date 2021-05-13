n = int(input())
prime = 0

def is_prime(q):
    if q == 2:
        return True
    if q < 2:
        return False
    return pow(2, q-1, q) == 1


prime = 0
for i in range(n):
    m = int(input())
    if is_prime(m):
        prime += 1
print(prime)