import sys


def slove():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    ls = [10 ** 10] * n
    t = 0
    for i in range(n):
        t += a[i]
    t /= n
    mt = 10 ** 10
    for i in range(n):
        ls[i] = abs(a[i] - t)
        mt = min(mt, ls[i])
    for i in range(n):
        if ls[i] == mt:
            print(i)
            exit()


if __name__ == '__main__':
    slove()
