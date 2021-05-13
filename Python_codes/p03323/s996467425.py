import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = mapint()
if A>8 or B>8:
    print(':(')
else:
    print('Yay!')