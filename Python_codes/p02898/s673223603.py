import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
sys.setrecursionlimit(10**9)


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy

N, K = map(int, input().split())
h = list(map(int, input().split()))
ans = 0
for hi in h:
    if hi >= K:
        ans += 1
print(ans)
