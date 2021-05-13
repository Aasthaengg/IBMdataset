import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def factorize_dict(n):
    b = 2
    fct = defaultdict(lambda: 0)
    while b ** 2 <= n:
        while n % b == 0:
            n //= b
            fct[b] += 1
        b += 1
    if n > 1:
        fct[n] += 1
    return fct


def main():

    N = in_n()

    if N == 1:
        print(0)
        exit()

    prime = defaultdict(int)
    for i in range(1, N + 1):
        for k, v in factorize_dict(i).items():
            prime[k] += v

    n2, n4, n14, n24, n74 = 0, 0, 0, 0, 0
    for k, v in prime.items():
        if v >= 2:
            n2 += 1
        if v >= 4:
            n4 += 1
        if v >= 14:
            n14 += 1
        if v >= 24:
            n24 += 1
        if v >= 74:
            n74 += 1

    ans = n74
    if n24 >= 1:
        ans += n24 * (n2 - 1)
    if n14 >= 1:
        ans += n14 * (n4 - 1)
    if n4 >= 2:
        ans += n4 * (n4 - 1) // 2 * (n2 - 2)
    print(ans)


if __name__ == '__main__':
    main()
