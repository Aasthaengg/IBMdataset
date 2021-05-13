printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

h,w = inm()
s = []
for i in range(h):
    s.append(ins())
a = [[0]*w for i in range(h)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]
id = 0
for i in range(h):
    for j in range(w):
        if a[i][j]!=0:
            continue
        id += 1
        a[i][j] = id
        q = [(i,j)]
        while len(q)>0:
            x,y = q.pop()
            c = s[x][y]
            for d in dir:
                u = x+d[0]
                v = y+d[1]
                if 0<=u<h and 0<=v<w and \
                   a[u][v]==0 and s[u][v]!=c:
                    a[u][v] = id
                    q.append((u,v))
bk = [0]*(id+1)
wh = [0]*(id+1)
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            bk[a[i][j]] += 1
        else:
            wh[a[i][j]] += 1
print(sum([bk[i]*wh[i] for i in range(1,id+1)]))
