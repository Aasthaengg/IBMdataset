import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = map(int, read().split())

    pos = [a for a in A if a >= 0]
    neg = [a for a in A if a < 0]

    pos.sort()
    neg.sort(reverse=True)

    if N == K:
        vec = A
    elif N == len(neg):
        if K & 1:
            vec = neg[:K]
        else:
            vec = neg[-K:]
    else:
        vec = []
        if K & 1:
            vec.append(pos.pop())

        tmp = []
        while len(neg) >= 2:
            tmp.append(neg.pop() * neg.pop())
        while len(pos) >= 2:
            tmp.append(pos.pop() * pos.pop())

        tmp.sort(reverse=True)
        vec.extend(tmp[: K // 2])

    ans = 1
    for a in vec:
        ans = ans * a % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
