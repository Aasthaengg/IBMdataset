# n以下の非負整数が素数かどうかを示すリストを返す
def primes(n):
    is_prime = [False] * 2 + [True] * (n - 1)
    for i in [2] + list(range(3, int(n ** 0.5) + 1, 2)):
        if not is_prime[i]: continue
        for j in range(2 * i, n + 1 ,i):
            is_prime[j] = False
    return is_prime

N = 10 ** 5
Q = int(input())
is_prime = primes(N)
cum2017 = [0] * (N + 1) # 累積和
for i in range(1, N + 1):
    cum2017[i] = cum2017[i - 1]
    if i % 2 == 1 and is_prime[i] and is_prime[(i + 1) // 2]:
        cum2017[i] += 1

for _ in range(Q):
    l, r = [int(x) for x in input().split()]
    print(cum2017[r] - cum2017[l - 1])