import sys


def solve(m, a, s):
    for i in range(m):
        if a[i] * 4 * m < s:
            return False
    return True


def main():
    input = sys.stdin.buffer.readline
    _, m = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    s = sum(a)
    print('Yes' if solve(m, a, s) else 'No')


if __name__ == '__main__':
    main()
