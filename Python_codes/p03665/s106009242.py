import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


N, P = readnums()
A = map(lambda x: x % 2, readnums())

if P:
    if not sum(A):
        print(0)
    else:
        print(2 ** N // 2)
else:
    if not sum(A):
        print(2 ** N)
    else:
        print(2 ** N // 2)
