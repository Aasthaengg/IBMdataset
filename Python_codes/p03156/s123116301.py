import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    n = int(input())
    a, b = map(int, input().split())
    P = list(map(int, input().split()))
    L = [0, 0, 0]
    for i in range(n):
        if P[i] <= a:
            L[0] += 1
        elif a+1 <= P[i] <= b:
            L[1] += 1
        else:
            L[2] += 1
    print(min(L))


resolve()