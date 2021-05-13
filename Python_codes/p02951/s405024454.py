import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, C = mapint()
print(max(C-(A-B), 0))