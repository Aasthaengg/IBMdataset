# エラトステネスの篩, 累積和
def make_prime_table(N):
    sieve = [0] * (N + 1)
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, N + 1):
        if sieve[i] != 0:
            continue
        sieve[i] = i
        for j in range(i * i, N + 1, i):
            if sieve[j] == 0:
                sieve[j] = i
    return sieve

max_lr = 10 ** 5

prime_table = make_prime_table(max_lr)

cs = [0] * (max_lr + 1)
for i in range(3, max_lr + 1, 2):
    if prime_table[i] == i and prime_table[(i + 1) // 2] == (i + 1) // 2:
        cs[i] = 1
for i in range(1, max_lr + 1):
    cs[i] += cs[i - 1]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(cs[r] - cs[l - 1])
