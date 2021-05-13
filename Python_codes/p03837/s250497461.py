from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,m = inm()
dst = {}
for i in range(m):
    a,b,c = inm()
    if a not in dst:
        dst[a] = {}
    dst[a][b] = c
    if b not in dst:
        dst[b] = {}
    dst[b][a] = c
d = [[BIG]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    d[i][i] = 0
    for j in dst[i]:
        d[i][j] = dst[i][j]
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
sm = 0
for i in range(1,n):
    for j in range(i+1,n+1):
        if j in dst[i] and dst[i][j]>d[i][j]:
            sm += 1
print(sm)
