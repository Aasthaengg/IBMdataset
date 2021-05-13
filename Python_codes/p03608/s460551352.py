from sys import stdout
import itertools
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

n,m,rr = inm()
r = inl()
r = [x-1 for x in r]
dst = [ [] for i in range(n) ]
for i in range(m):
    a,b,c = inm()
    dst[a-1].append((b-1,c))
    dst[b-1].append((a-1,c))

ddprint("n {} m {} r {}".format(n,m,rr))
ddprint(dst)

# warshal floyd
dist = [ [BIG]*n for i in range(n) ]
for i in range(n):
    dist[i][i] = 0
    for j,c in dst[i]:
        dist[i][j] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

ddprint("dist")
ddprint(dist)

pm = itertools.permutations(r,rr)
mn = BIG
for p in pm:
    sm = 0
    #ddprint(p)
    for i in range(rr-1):
        sm += dist[p[i]][p[i+1]]
    mn = min(mn,sm)
print(mn)
