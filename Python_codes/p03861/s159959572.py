import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    a, b, x = in_nn()
    ans = b // x
    if a == 0:
        ans += 1
    else:
        ans -= (a - 1) // x
    print(ans)


if __name__ == '__main__':
    main()
