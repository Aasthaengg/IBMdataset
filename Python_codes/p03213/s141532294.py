import math
N = int(input())


def trial_division(n):
    # 2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            primes[num] += 1
    # リストが空ならそれは素数
    if n != 1:
        primes[n] += 1
        return


primes = [0 for _ in range(N+1)]
for i in range(2, N+1):
    trial_division(i)

P74, P24, P14, P4, P2 = 0, 0, 0, 0, 0
for i in range(2, N+1):
    if primes[i] >= 74:
        P74 += 1
    if primes[i] >= 24:
        P24 += 1
    if primes[i] >= 14:
        P14 += 1
    if primes[i] >= 4:
        P4 += 1
    if primes[i] >= 2:
        P2 += 1

ans = 0
ans += P4*(P4-1)//2*(P2-2)
ans += P14*(P4-1)
ans += P24*(P2-1)
ans += P74
print(ans)
