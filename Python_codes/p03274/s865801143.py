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
    x = in_nl()

    ans = 10**9 + 7
    for i in range(N - K + 1):
        left = x[i]
        right = x[i + K - 1]
        if right <= 0:
            ans = min(ans, abs(left))
        elif left >= 0:
            ans = min(ans, abs(right))
        else:
            ans = min(ans, abs(left) + abs(right) + min(abs(left), abs(right)))

    print(ans)


if __name__ == '__main__':
    main()
