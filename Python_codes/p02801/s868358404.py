import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    c = input()
    ans = chr(ord(c) + 1)
    print(ans)


if __name__ == '__main__':
    solve()
