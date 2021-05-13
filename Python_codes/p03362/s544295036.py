n = 55555
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes=list(primes)

N = int(input())
ans = []
cnt = 0
for p in primes:
    if p % 5 == 1:
        ans += [p]
        cnt += 1
    if cnt == N:
        break

for p in ans:
    print(p, end=" ")
