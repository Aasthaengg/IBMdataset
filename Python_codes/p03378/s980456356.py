import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, X = mapint()
As = set(list(mapint()))
to_zero = 0
for i in range(X, 0, -1):
    if i in As:
        to_zero += 1

to_N = 0
for i in range(X, N+1):
    if i in As:
        to_N += 1
print(min(to_zero, to_N))