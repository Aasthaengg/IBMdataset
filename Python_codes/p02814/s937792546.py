from collections import defaultdict

#素数リスト
def prime_list(n=10**6+1):
    res = []
    tmp = [1 for _ in range(n)]
    tmp[0] = 0
    tmp[1] = 0
    i = 2
    while i < len(tmp):
        j = i*2
        while tmp[i] == 1 and j < len(tmp):
            tmp[j] = 0
            j += i
        i += 1

    for i, j in enumerate(tmp):
        if j:
            res.append(i)

    return res
prime_number = prime_list()

def prime_fact(n):
    primes = []
    for i in prime_number:
        tmp = 0
        while n % i == 0:
            tmp += 1
            n //= i
        if tmp != 0:
            primes.append([i, tmp])
        if i * i > n:
            break

    if n != 1:
        primes.append([n, 1])
    return primes

n, m = map(int, input().split())
a = list(map(int, input().split()))

so = defaultdict(int)

two = []
for i in a:
    if i % 2 != 0:
        print(0)
        exit()

    primes = prime_fact(i)
    for k, v in primes:
        if k == 2:
            if len(two) != 0 and two[-1] != v:
                print(0)
                exit()
            two.append(v)
        so[k] = max(so[k], v)

tmp = 1
for i, j in so.items():
    tmp *= i ** j
    if tmp > 2 * m:
        print(0)
        exit()

tmp //= 2
# print(tmp)
ans = m // tmp

if ans % 2 == 0:
    ans //= 2
else:
    ans //=2
    ans += 1

print(ans)

