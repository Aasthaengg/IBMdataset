import math
n = int(input())
v = []

for _ in range(n):
    v.append(int(input()))

n_prime = 0
for v_ in v:
    isprime = True

    if v_ <= 1:
        continue

    for i in range(1+int(math.sqrt(v_))):
        if i <= 1:
            continue
        if v_ % i == 0:
            isprime = False
            break

    n_prime = n_prime + isprime

print(n_prime)
