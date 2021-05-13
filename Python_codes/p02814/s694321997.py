import sys
from fractions import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def lcm(x, y):
    return x * y // gcd(x, y)


def f(a):
    ans = 0
    while a % 2 == 0:
        a //= 2
        ans += 1
    return ans


def main():
    N, M, *A = map(int, read().split())
    A = [a // 2 for a in A]

    p2 = f(A[0])
    for a in A[1:]:
        if p2 != f(a):
            print(0)
            return

    semi_lcm = A[0]
    for a in A[1:]:
        semi_lcm = lcm(semi_lcm, a)

    print((M // semi_lcm + 1) // 2)
    return


if __name__ == '__main__':
    main()
