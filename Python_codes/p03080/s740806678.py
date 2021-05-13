import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    s = str(input().rstrip('\n'))
    print("Yes" if s.count("R") > s.count("B") else "No")


if __name__ == '__main__':
    solve()
