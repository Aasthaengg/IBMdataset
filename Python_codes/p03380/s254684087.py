import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    n = in_n()
    a = sorted(in_nl())

    a_max = a[-1]
    diff = 10**9 + 7
    for i in range(n - 1):
        t = abs(a_max / 2 - a[i])
        if t < diff:
            a_mid = a[i]
            diff = t

    print(a_max, a_mid)


if __name__ == '__main__':
    main()
