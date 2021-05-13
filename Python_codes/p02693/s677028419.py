import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    k = int(readline())
    a, b = list(map(int, readline().split()))
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            exit()
    print("NG")


if __name__ == '__main__':
    solve()
