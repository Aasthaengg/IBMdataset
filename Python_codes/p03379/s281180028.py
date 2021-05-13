import sys


def input(): return sys.stdin.readline().strip()


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    lsort = sorted(l)
    left = lsort[n // 2 - 1]
    right = lsort[n // 2]
    for i in l:
        if i <= left:
            print(right)
        else:
            print(left)
resolve()