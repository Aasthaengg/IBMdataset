import sys
import math

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, P = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    odd = 0
    even = 0
    ans = 0
    def comb(n, r):
        return math.factorial(n) // math.factorial(r) // math.factorial(n - r)
    for a in A:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1

    if P == 0:
        for i in range(0, odd + 1, 2):
            for j in range(even + 1):
                ans += comb(odd, i) * comb(even, j)
        print(ans)
    else:
        for i in range(1, odd + 1, 2):
            for j in range(even + 1):
                ans += comb(odd, i) * comb(even, j)
        print(ans)


if __name__ == '__main__':
    main()
