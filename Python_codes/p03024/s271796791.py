import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    s = str(input().rstrip('\n'))
    print("YES" if s.count("x") < 8 else "NO")


if __name__ == '__main__':
    solve()
