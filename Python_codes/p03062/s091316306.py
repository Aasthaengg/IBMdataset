import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    total = 0
    mi = f_inf
    for a in A:
        total += abs(a)
        if a < 0:
            cnt += 1
        if mi > abs(a):
            mi = abs(a)

    if cnt % 2 == 0:
        print(total)
    else:
        print(total - mi * 2)


if __name__ == '__main__':
    resolve()
