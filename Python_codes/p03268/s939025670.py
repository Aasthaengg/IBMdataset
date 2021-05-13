import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    ls = []
    for i in range(1, n + 1):
        ls.append(i % k)
    h = 0
    j = 0
    for v in ls:
        if v == 0:
            j += 1
        if v * 2 == k:
            h += 1
    print(j ** 3 + h ** 3)


if __name__ == '__main__':
    solve()
