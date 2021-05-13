import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, M = in_nn()
    if N == 1 and M == 1:
        ans = 1
    elif N == 1 and M > 1:
        ans = M - 2
    elif N > 1 and M == 1:
        ans = N - 2
    else:
        ans = (N - 2) * (M - 2)
    print(ans)


if __name__ == '__main__':
    main()
