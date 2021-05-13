from collections import deque
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

h,w = inm()
s = []
nb = 0
for i in range(h):
    ss = ins()
    s.append(ss)
    nb += ss.count('#')
q = deque([(0,0)])
d = [[BIG]*w for i in range(h)]
d[0][0] = 0
while len(q)>0:
    x,y = q.popleft()
    dd = d[x][y]
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        xx = x+dx
        yy = y+dy
        if 0<=xx<h and 0<=yy<w and s[xx][yy]=='.' and d[xx][yy]>dd+1:
            d[xx][yy] = dd+1
            q.append((xx,yy))
z = d[h-1][w-1]
print(-1 if z==BIG else (h*w-nb-z-1))
