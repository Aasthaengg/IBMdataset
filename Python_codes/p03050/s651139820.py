N = int(input())


def divisors(n, sort=False):
    """
    nの約数をO(√n)で列挙する
    """
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    if sort:
        d.sort()
    return d


ans = 0
for d in divisors(N):
    if d == 1:
        continue
    m = d - 1
    if N // m == N % m:
        ans += m
print(ans)