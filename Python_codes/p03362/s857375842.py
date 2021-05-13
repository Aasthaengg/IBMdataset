# n以下の素数を求める エラトステネスの篩
def primes(n):
    is_prime = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1): # 素数候補
        if not is_prime[i]: continue
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
n = 1450  # n = 1450以下の素数pのうち p mod 5 = 1となるpは55個ある
P = primes(n)

A = []
for p in P:
    if p % 5 == 1:
        A.append(str(p))

print(" ".join(A[0:N]))