import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

x, y = mapint()
cnt = 0
if x*y>0:
    if y<x:
        cnt += 2
    cnt += abs(x-y)
elif x*y==0:
    if x<y:
        cnt = y-x
    else:
        cnt = (x-y)+1
else:
    cnt += 1
    x *= -1
    cnt += abs(x-y)
print(cnt)