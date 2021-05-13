import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = mapint()
if abs(A-B)%2==1:
    print('IMPOSSIBLE')
else:
    print((A+B)//2)