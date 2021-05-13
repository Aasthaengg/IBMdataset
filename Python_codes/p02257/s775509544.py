import math
N = input()
pnum_count = N
for _ in range(N):
    n = input()
    if n == 2:
        continue
    if n % 2 == 0:
        pnum_count -= 1
        continue
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            pnum_count -= 1
            break
        i += 1
print pnum_count