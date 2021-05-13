import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    if N==1:
        print('a')
    else:
        q = ['a']
        for _ in range(N - 1):
            nq = []
            for j in q:
                for k in range(ord('a'), ord(max(j)) + 2):
                    nq.append(j + chr(k))
            q=nq

        print(*q,sep='\n')

resolve()