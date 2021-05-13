import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    K, T = in_nn()
    a = in_nl()
    maxA = max(a)
    mT = -(-K // 2)
    ans = max(0, (maxA - mT) * 2 - 1)
    print(ans)


if __name__ == '__main__':
    main()
