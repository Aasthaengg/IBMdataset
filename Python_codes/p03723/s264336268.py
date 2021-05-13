import random as rng
import itertools as it
import collections as col
import heapq as hq
import sys
import copy as cp
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dump_impl(*objects):
    print(*objects, file=sys.stderr)


def dump_dummy(*objects):
    pass


dump = dump_impl if "DEBUG" in sys.argv else dump_dummy


def odd(n): return n & 1


def even(n): return not odd(n)


A, B, C = map(int, input().split())
ans = 0
a, b, c = A, B, C
while True:
    dump(a, b, c)
    if odd(a) or odd(b) or odd(c):
        print(ans)
        exit()
    if ans > 0 and a == A and b == B and c == C:
        print(-1)
        exit()
    a, b, c = (b+c)//2, (a+c)//2, (a+b)//2
    ans += 1
