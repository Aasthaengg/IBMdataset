

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def primes(N):
    is_prime = [True]*(N+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, N+1):
        if is_prime[i]:
            for j in range(2*i, N+1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p and i%5 == 1]


def solve():
    N = read_int()
    some_primes = primes(2000)
    print(*some_primes[:N])


if __name__ == '__main__':
    solve()
