from collections import deque
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**7
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

h,w = inm()
s = []
for i in range(h):
    s.append(ins())
d = [[BIG]*w for i in range(h)]
z = 1 if s[0][0]=='#' else 0
q = deque([(0,0,z)])
while len(q)>0:
    x,y,z = q.popleft()
    #ddprint(f"1 {x=} {y=} {z=} {d=}")
    if z>=d[x][y]:
        continue
    #ddprint(d[x])
    d[x][y] = z
    incx = 1 if x<h-1 and s[x+1][y]=='#' and s[x][y]=='.' else 0
    incy = 1 if y<w-1 and s[x][y+1]=='#' and s[x][y]=='.' else 0
    if x<h-1 and d[x+1][y]>z+incx:
        q.append((x+1,y,z+incx))
    if y<w-1 and d[x][y+1]>z+incy:
        q.append((x,y+1,z+incy))
print(d[h-1][w-1])
