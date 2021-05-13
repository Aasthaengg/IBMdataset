import sys


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    s = str(input().rstrip('\n'))
    print("YES" if s.count("o") >= 8 - (15 - len(s)) else "NO")


if __name__ == '__main__':
    slove()
