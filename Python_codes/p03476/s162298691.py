from bisect import bisect_left


def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def is_similar(n):
    pos = bisect_left(p, n)
    if pos < len(p) and p[pos] == n:
        return True
    else:
        return False


q = int(input())

p = primes(10 ** 5)
l = [0] * 10 ** 5
for i in range(3, 10 ** 5, 2):
    if is_similar(i) and is_similar((i+1)//2):
        l[i] += 1

sum_l = [0]
for v in l[1:]:
    sum_l.append(sum_l[-1] + v)

res = []
for _ in range(q):
    l, r = map(int, input().split())
    res.append(sum_l[r] - sum_l[l-1])

for v in res:
    print(v)