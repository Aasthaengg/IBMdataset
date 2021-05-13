import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    x1, y1, x2, y2 = in_nn()

    ans = 'R' * (x2 - x1) + 'U' * (y2 - y1)
    ans += 'L' * (x2 - x1) + 'D' * (y2 - y1)
    ans += 'L'
    ans += 'U' * (y2 - y1 + 1) + 'R' * (x2 - x1 + 1)
    ans += 'D'
    ans += 'R'
    ans += 'D' * (y2 - y1 + 1) + 'L' * (x2 - x1 + 1)
    ans += 'U'

    print(ans)


if __name__ == '__main__':
    main()
