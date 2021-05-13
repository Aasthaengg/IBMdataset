import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())


# bit全探索で愚直に
def solver1(n, p, A):
    ans = 0
    for i in range(2**n):
        x = 0
        for j in range(n):
            if (i>>j) & 1:
                x += A[j]
        if x % 2 == p:
            ans += 1
    return ans


def solver2(n, p, A):
    odd = 0
    even = 0
    for a in A:
        if a % 2 == 1:
            odd += 1
        else:
            even += 1
    if odd == 0:
        if p == 0:
            return 2 ** even
        else:
            return 0
    else:
        return 2 ** (n-1)


def main():
    n, p = inintm()
    A = inintl()
    # print(solver1(n, p, A))
    print(solver2(n, p, A))


main()
