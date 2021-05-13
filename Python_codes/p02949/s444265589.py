from collections import deque #,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,m,p = inm()
dst = [{} for i in range(n+1)]
src = [{} for i in range(n+1)]
es = []
for i in range(m):
    a,b,c = inm()
    dst[a][b] = src[b][a] = p-c
    es.append((a,b,p-c))

rf1 = [False]*(n+1)
rf1[1] = True
q = deque([1])
while len(q)>0:
    x = q.popleft()
    for y in dst[x]:
        if not rf1[y]:
            rf1[y] = True
            q.append(y)

rtn = [False]*(n+1)
rtn[n] = True
q = deque([n])
while len(q)>0:
    x = q.popleft()
    for y in src[x]:
        if not rtn[y]:
            rtn[y] = True
            q.append(y)

ddprint(rf1)
ddprint(rtn)

use = [rf1[i] and rtn[i] for i in range(n+1)]

es = [z for z in es if use[z[0]] and use[z[1]]]
ddprint(es)

dp = [BIG]*(n+1)
dp[1] = 0
for i in range(n):
    ddprint(dp)
    for a,b,c in es:
        if dp[b] > dp[a]+c:
            dp[b] = dp[a]+c
            if i==n-1:
                print(-1)
                exit()

print(max(0,-dp[n]))
