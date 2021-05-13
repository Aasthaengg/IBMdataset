import sys

N = int(sys.stdin.readline())

primes = set()
exists = set()
for i in range(2, 55555):
    if i in exists:
        continue
    primes.add(i)
    for j in range(i, 55555, i):
        if j in exists:
            continue
        exists.add(j)

# % 5 == 1となるもの
ans = []
for prime in primes:
    if prime % 5 == 1:
        ans.append(prime)
    if len(ans) == N:
        break

print(*ans)