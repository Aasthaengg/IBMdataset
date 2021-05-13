import sys
def input(): return sys.stdin.readline().strip()

mi = lambda: map(int, input().split())

M, N = mi()

print(M-N+1)