import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, s, C = input().split()
print(''.join([A[0], s[0], C[0]]))