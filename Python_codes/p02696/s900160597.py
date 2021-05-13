import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, N = mapint()
x = min(B-1, N)
print(int(A*x/B)-A*int(x/B))