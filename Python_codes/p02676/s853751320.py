import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


K = ni()
S = ns()
if K >= len(S):
    print(S)
else:
    print(S[:K] + "...")
