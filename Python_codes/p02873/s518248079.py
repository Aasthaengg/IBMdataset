import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    S = gete()

    p = []
    nl, ng = 0, 0  # <, >

    for i, c in enumerate(S):
        if c == "<":
            nl += 1
        else:
            ng += 1

        if c == "<" and i < len(S) - 1 and S[i + 1] == ">":
            p.append((ng, nl))
            nl, ng = 0, 0

    p.append((ng, nl))

    ans = 0
    for i, q in enumerate(p):

        if i == 0 or p[i - 1][1] < q[0]:
            ans += q[0] * (q[0] + 1) // 2
        else:
            ans += q[0] * (q[0] - 1) // 2

        if i == len(p) - 1 or q[1] >= p[i + 1][0]:
            ans += q[1] * (q[1] + 1) // 2
        else:
            ans += q[1] * (q[1] - 1) // 2


    print(ans)


if __name__ == "__main__":
    main()