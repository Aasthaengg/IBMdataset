import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = str(readline().rstrip().decode('utf-8'))
    print(n.count("2"))


if __name__ == '__main__':
    solve()
