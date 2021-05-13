import sys


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    na = 1
    nb = 1
    for i in range(n):
        t, a = list(map(int, input().rstrip('\n').split()))
        r = max((na + t - 1) // t, (nb + a - 1) // a)
        na = r * t
        nb = r * a
    print(na + nb)


if __name__ == '__main__':
    slove()
