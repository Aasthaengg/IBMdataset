from copy import copy

def make_divisors(n):
    """約数を全列挙する
    """
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


N0 = int(input())
cand = set(make_divisors(N0) + make_divisors(N0-1))

ans = 0
for K in cand:
    if K == 1:
        continue
    N = copy(N0)
    while N%K == 0:
        N //= K
    N %= K
    if N == 1:
        ans += 1

print(ans)
