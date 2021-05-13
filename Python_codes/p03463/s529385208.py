import sys


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, a, b = list(map(int, input().rstrip('\n').split()))
    if (a - b) % 2 == 0:
        print("Alice")
    else:
        print("Borys")


if __name__ == '__main__':
    slove()
