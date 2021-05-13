import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    t1, t2 = list(map(int, readline().split()))
    a1, a2 = list(map(int, readline().split()))
    b1, b2 = list(map(int, readline().split()))
    a1 -= b1
    a2 -= b2
    if a1 * t1 + a2 * t2 == 0:
        print("infinity")
        exit()
    elif a1 < 0:
        if a1 * t1 + a2 * t2 < 0:
            print(0)
            exit()
    elif a1 > 0:
        if a1 * t1 + a2 * t2 > 0:
            print(0)
            exit()
    s = abs(a1 * t1) // abs(a1 * t1 + a2 * t2)
    m = abs(a1 * t1) % abs(a1 * t1 + a2 * t2)
    print(s * 2 if m == 0 else s * 2 + 1)


if __name__ == '__main__':
    solve()
