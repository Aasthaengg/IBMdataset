import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    X = str(input())
    stack = 0
    pop = 0
    for i in range(len(X)):
        if X[i] == 'S':
            stack += 1
        elif X[i] == 'T' and stack > 0:
            pop += 1
            stack -= 1
    print(len(X)-pop*2)

resolve()