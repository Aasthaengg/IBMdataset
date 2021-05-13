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
    h = sorted(list(in_na()))

    ans = 10**9 + 7

    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])

    print(ans)


if __name__ == '__main__':
    main()
