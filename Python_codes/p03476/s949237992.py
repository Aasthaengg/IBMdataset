def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]: ass.append(i)
    return ass

d = primes(10**5)
d2017 = []
for i in d:
    if i > 10**5: break
    if (i+1)//2 in d:
        d2017.append(i)

import bisect
q = int(input())
ans = 0
for _ in range(q):
    l, r = map(int, input().split())
    index_l = bisect.bisect_left(d2017, l-1)
    index_r = bisect.bisect_right(d2017, r)
    print(index_r-index_l)