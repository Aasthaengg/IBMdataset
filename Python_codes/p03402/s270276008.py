import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

a, b = [int(_) for _ in input().split()]

a -= 1
b -= 1


def f(b, av, bv):
    A = [list(av * 100) for _ in range(50)]
    for i in range(1, 49):
        if b == 0: break
        for j in range(1, 99):
            if b == 0: break

            if A[i - 1][j] != bv and \
                    A[i - 1][j - 1] != bv and \
                    A[i - 1][j + 1] != bv and \
                    A[i][j - 1] != bv :
                A[i][j] = bv
                b -= 1
    for a in A:
        print(*a,sep='')

print(100,100)
f(b, '.', '#')
f(a, '#', '.')
