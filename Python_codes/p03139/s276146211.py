import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()
print(min(A, B), max((A+B-N), 0))