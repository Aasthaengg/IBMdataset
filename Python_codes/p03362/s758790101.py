# 17:49
def seive(n):
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0
    return is_prime


N = int(input())
cands = [i for i, p in enumerate(seive(1381)) if p and i % 5 == 1]
print(*cands[:N])
