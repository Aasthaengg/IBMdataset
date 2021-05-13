import sys


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    a, b, k = list(map(int, input().rstrip('\n').split()))
    for i in range(k):
        if i % 2 == 0:
            if a % 2 != 0:
                a -= 1
            b += a // 2
            a -= a // 2
        else:
            if b % 2 != 0:
                b -= 1
            a += b // 2
            b -= b // 2
    print(a, b)


if __name__ == '__main__':
    slove()
