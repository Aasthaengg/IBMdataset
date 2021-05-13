import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X, A = mapint()
if X<A:
    print(0)
else:
    print(10)