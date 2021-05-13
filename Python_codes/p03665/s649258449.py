import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def comb(n, k):

    k = min(k, n - k)

    m = 1
    for i in range(n, n - k, -1):
        m *= i

    n = 1
    for i in range(1, k + 1):
        n *= i

    return m // n


def main():
    N, P = in_nn()
    A = in_nl()

    odd = 0
    even = 0
    for a in A:
        if a % 2 == 0:
            odd += 1
        else:
            even += 1

    #print(odd, even)

    ans = 0
    if P == 0:
        for k in range(0, even + 1, 2):
            ans += comb(even, k) * 2**odd
    else:
        for k in range(1, even + 1, 2):
            ans += comb(even, k) * 2**odd

    print(ans)


if __name__ == '__main__':
    main()
