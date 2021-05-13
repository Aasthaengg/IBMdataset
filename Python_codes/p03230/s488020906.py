import math
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())


def solve(N):
    count = math.ceil(math.sqrt(N * 2))
    if count * (count - 1) != N * 2 or N == 2:
        return []

    ans = [[] for _ in range(count)]
    a = 1
    for i in range(count):
        for j in range(count - 1 - len(ans[i])):
            ans[i].append(a)
            ans[i + 1 + j].append(a)
            a += 1

    return ans


ans = solve(N)
if ans:
    print('Yes')
    cnt = len(ans)
    print(cnt)
    for r in ans:
        print(cnt - 1, *r)
else:
    print('No')
