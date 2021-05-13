import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

s = ns()

a = s.count('a')
b = s.count('b')
c = s.count('c')

print('YES' if max(a, b, c) <= min(a, b, c) + 1 else 'NO')