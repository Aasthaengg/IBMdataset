import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N, K = in_nn()
    readline()

    if K == 2:
        print(N - 1)
        exit()

    q, r = divmod(N, K - 1)
    if r in (0, 1):
        ans = q
    else:
        ans = q + 1

    print(ans)


if __name__ == '__main__':
    main()
