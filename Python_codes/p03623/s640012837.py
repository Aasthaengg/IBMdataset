import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

x, a, b = mapint()
if abs(x-a)>abs(x-b):
    print('B')
else:
    print('A')