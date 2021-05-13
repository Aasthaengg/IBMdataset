import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = sorted(list(map(str, readline().rstrip().decode('utf-8').split())))
    print("YES" if n == sorted("1974") else "NO")


if __name__ == '__main__':
    solve()
