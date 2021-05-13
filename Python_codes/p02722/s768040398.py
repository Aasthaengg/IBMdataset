n = int(input())


def check(n, k):
    while n % k == 0:
        n = n // k
    if n >= k:
        n = n - k * (n // k)
    return n


def count(n):
    total = 0
    cands = set([n, n-1])
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cands.add(i)
            cands.add(n // i)
    for i in range(2, int(n ** 0.5) + 1):
        if (n-1) % i == 0:
            cands.add(i)
            cands.add((n - 1) // i)
    for k in cands:
        if k == 1:
            continue
        if check(n, k) == 1:
            total += 1
    return total


print(count(n))