def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

A = []
count = 0
for a in range(55556):
    if a % 5 != 1:
        continue
    if isprime(a):
        A.append(a)
        count += 1
    if count == n:
        break

print(*A)
