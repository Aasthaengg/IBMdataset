from collections import Counter, defaultdict

N = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

primes = []
for i in range(2, N + 1):
    primes += prime_factorize(i)

counters = Counter(primes)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

divisors = make_divisors(75)
cnt = defaultdict(int)
for k, v in counters.items():
    for d in divisors:
        if v + 1 >= d:
            cnt[d] += 1     
print(cnt[75] + cnt[25] * (cnt[3] - 1) + cnt[15] * (cnt[5] - 1)
+ max(cnt[5] * (cnt[5] - 1) * (cnt[3] - 2) // 2, 0))