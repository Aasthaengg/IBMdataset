import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


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


def main():

    N = in_n()
    p_list = primes(55555)
    M = len(p_list)

    ans = []
    for i in range(M):
        if p_list[i] % 5 == 1:
            ans.append(p_list[i])

    print(' '.join(map(str, (ans[:N]))))


if __name__ == '__main__':
    main()
