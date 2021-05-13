import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    LL = []
    for i in range(N):
        L = list(map(int, input().split()))
        LL.append(L + [sum(L)])

    LL = sorted(LL, key=lambda x: x[2],reverse=True)

    cntA = 0
    cntT = 0
    for i in range(len(LL)):
        if i % 2 == 0:
            cntT += LL[i][0]
        else:
            cntA += LL[i][1]
    print(cntT - cntA)


resolve()