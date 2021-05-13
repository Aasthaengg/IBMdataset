import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, C = mapint()
xv = [list(mapint()) for _ in range(N)]
righthand = [0]*N
lefthand = [0]*N
nowv = 0
maxv = -10**18
for i, (x, v) in enumerate(xv):
    nowv += v
    maxv = max(maxv, nowv-x)
    righthand[i] = maxv
nowv = 0
maxv = -10**18
for i, (x, v) in enumerate(xv[::-1]):
    nowv += v
    maxv = max(maxv, nowv-(C-x))
    lefthand[i] = maxv
 
xv = [(0, 0)] + xv +[(C, 0)]
righthand = [0]+righthand
lefthand = [0]+lefthand
rmax = 0
for i in range(N+1):
    rmax = max(rmax, righthand[i]-xv[i][0]+lefthand[N-i])
lmax = 0
for i in range(N):
    lmax = max(lmax, lefthand[i]-(C-xv[-i-1][0])+righthand[N-i])
print(max(rmax, lmax))