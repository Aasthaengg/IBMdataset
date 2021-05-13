def permu(n,r,p):
    result = 1
    for i in range(n,n-r,-1):
        result *= i
        result %= p
    return result

from collections import deque

n,k = map(int,input().split())
mod = 10**9 + 7
G = [[] for i in range(n)]
for i in range(n-1):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    G[x].append(y)
    G[y].append(x)

ans = k
s = True
que = deque([[-1,0]])
while que:
    pre,now = que.pop()

    if s:
        s = False
        ans *= permu(k-1,len(G[0]),mod)
        for nex in G[0]:
            que.append([0,nex])

    else:
        ans *= permu(k-2,len(G[now])-1,mod)
        for nex in G[now]:
            if nex == pre:continue
            que.append([now,nex])
    ans %= mod

print(ans)