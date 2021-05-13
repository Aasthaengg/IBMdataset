import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    s = str(readline().rstrip().decode('utf-8'))
    if len(s) == 2:
        print(s)
    else:
        s = list(s)
        s.reverse()
        print("".join(s))


if __name__ == '__main__':
    solve()
