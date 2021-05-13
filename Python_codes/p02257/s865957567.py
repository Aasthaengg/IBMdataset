def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

num = []
prime_numbers = []

n = int(input())

for _ in range(n):
    i = int(input())
    num.append(i)

for i in num:
    if is_prime(i):
        prime_numbers.append(i)

print(len(prime_numbers))