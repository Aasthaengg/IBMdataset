import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, C, D = mapint()
if A+B>C+D:
    print('Left')
elif A+B<C+D:
    print('Right')
else:
    print('Balanced')