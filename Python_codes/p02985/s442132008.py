import sys
from collections import deque
def chs(s,t,md):###chooseではない
    res = 1
    for i in range(s-t+1,s+1):
        res *= i
        res%=md
    """
    for i in range(1,t+1):
        i2 = pow(i,md-2,md)
        res*=i2
        res%=md
    """
    return(res)

mod = 10**9+7
n, k = map(int, input().split( ))
E = [[] for _ in range(n)]
Deg = [0]*n
for _ in range(n-1):
    a,b = map(int, input().split( ))
    a-=1
    b-=1
    E[a].append(b)
    E[b].append(a)

Done = [False]*n
dp = [1]*n

Q = deque()
#rootを0に指定
Q.append(0)
#outのDeg
Deg=[0]*n
P = [-1]*n
Done[0] = True

while Q:
    u = Q.popleft()
    for v in E[u]:
        if not Done[v]:
            Done[v] = True
            Deg[u] +=1
            if Deg[u]>k:
                print(0)
                sys.exit()
            P[v] = u
            Q.append(v)
ans = chs(k,Deg[0]+1,mod)###+1
e0 = set(E[0])
#print(k-1,Deg[0],ans)
for i in range(1,n):
    ans*=chs(k-2,Deg[i],mod)
    ans %=mod
    #print(i,Deg[i],ans)
print(ans)
