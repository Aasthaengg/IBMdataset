import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18

H, W, N = list(map(int, sys.stdin.readline().split()))
AB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

hist = set()


def count(h, w):
    ret = 0
    for dh, dw in itertools.product([-1, 0, 1], repeat=2):
        ret += (h + dh, w + dw) in hist
    return ret


def ok(a=1, b=1):
    return 1 < a < H and 1 < b < W


ans = [0] * 10
ans[0] = (H - 2) * (W - 2)
for a, b in AB:
    hist.add((a, b))
    for dh, dw in itertools.product([-1, 0, 1], repeat=2):
        if not ok(a + dh, b + dw):
            continue
        c = count(a + dh, b + dw)
        ans[c] += 1
        ans[c - 1] -= 1
print('\n'.join(map(str, ans)))
