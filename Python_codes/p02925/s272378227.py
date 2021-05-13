from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

#from collections import defaultdict,deque
n = inn()
pr = [[ [] for i in range(n+1) ] for j in range(n+1)]
ch = [[ [] for i in range(n+1) ] for j in range(n+1)]
for i in range(1,n+1):
    a = inl()
    for j in range(n-2):
        x1 = x2 = i
        y1 = a[j]
        y2 = a[j+1]
        if x1>y1:
            x1,y1 = y1,x1
        if x2>y2:
            x2,y2 = y2,x2
        ch[x1][y1].append((x2,y2))
        pr[x2][y2].append((x1,y1))
g = [ [0]*(n+1) for i in range(n+1) ]
q = []
for i in range(1,n):
    for j in range(i+1,n+1):
        if len(pr[i][j])==0:
            q.append((i,j))
            g[i][j] = 1
        else:
            g[i][j] = 0
ddprint(ch)
ddprint("pr")
ddprint(pr)
ddprint(g)
while len(q)>0:
    z = q.pop()
    i,j = z
    for u,v in ch[i][j]:
        g[u][v] = max(g[u][v], g[i][j]+1)
        #ddprint("y {} z {}".format(y,z))
        pr[u][v].remove(z)
        if len(pr[u][v])==0:
            #del pr[y]
            q.append((u,v))
ddprint("newg")
ddprint(g)
#gmn = [min(r[1:]) for r in g[1:]]
gmn = BIG
for i in range(1,n):
    for j in range(i+1,n+1):
        gmn = min(gmn,g[i][j])
if gmn==0:
    print(-1)
else:
    print(max([max(r) for r in g]))
