import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

W, H, N = mapint()
x1, y1 = 0, 0
x2, y2 = W, H
for _ in range(N):
    x, y, a = mapint()
    if a==1:
        x1 = max(x1, x)
    elif a==2:
        x2 = min(x2, x)
    elif a==3:
        y1 = max(y1, y)
    else:
        y2 = min(y2, y)

print(max(x2-x1, 0)*max(y2-y1, 0))