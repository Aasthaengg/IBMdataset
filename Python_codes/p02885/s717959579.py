import sys

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
print(max(0, A - B * 2))


