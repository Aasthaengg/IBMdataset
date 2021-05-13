import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

r, d, x = mapint()
for i in range(10):
    nx = r*x-d
    print(nx)
    x = nx