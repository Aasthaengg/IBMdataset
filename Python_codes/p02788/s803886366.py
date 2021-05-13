from collections import deque
import sys

input = sys.stdin.buffer.readline
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n, d, a = MAP()
xh = [LIST() for i in range(n)]

xh = sorted(xh, key=lambda x:(x[0]))
q = deque()
ca = 0
cnt = 0
for i in range(n):
    cx, ch = xh[i][0], xh[i][1]
    
    while q and q[0][0] < cx:
        qx, qa = q.popleft()
        ca -= qa
    
    if ch - ca <= 0:
        continue
    
    cn = (ch - ca + a - 1) // a
    cnt += cn
    ca += cn * a
    q.append([cx+2*d, cn*a])
    
print(cnt)