import sys
from fractions import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def lcm(x, y):
    return x * y // gcd(x, y)


def main():
    N, M = map(int, input().split())
    A = list(set(map(int, input().split(" "))))
    A = [a // 2 for a in A]
    semi_lcm = 1
    for a in A:
        semi_lcm = lcm(semi_lcm, a)
        if semi_lcm > M:
            print(0)
            return

    for a in A:
        if semi_lcm // a % 2 == 0:
            print(0)
            return

    print((M // semi_lcm + 1) // 2)
    return


if __name__ == '__main__':
    main()
