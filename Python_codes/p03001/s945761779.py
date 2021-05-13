import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

W, H, x, y = mapint()
if x==W/2 and y==H/2:
    print(W*H/2, 1)
else:
    print(W*H/2, 0)