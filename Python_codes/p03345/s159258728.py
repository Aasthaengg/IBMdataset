import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, C, K = mapint()
if K%2==0:
    print(A-B)
else:
    print(B-A)