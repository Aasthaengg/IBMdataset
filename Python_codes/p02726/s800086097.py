def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for _ in range(n)]
import math
from queue import deque
n,x,y = L()
g = [[] for _ in range(n)]
for i in range(n):
    if (i == x-1):
        if (i == 0):
            g[i] = [1,y-1]
        elif (i == n-1):
            g[i] = [i-1,y-1]
        else:
            g[i] = [i-1,i+1,y-1]
    elif (i == y-1):
        if (i == 0):
            g[i] = [1,x-1]
        elif (i == n-1):
            g[i] = [i-1,x-1]
        else:
            g[i] = [i-1,i+1,x-1]
    else:
        if (i == 0):
            g[i] = [1]
        elif (i == n-1):
            g[i] = [i-1]
        else:
            g[i] = [i-1,i+1]
#print(g)
dis = [[0]*n for i in range(n)]
#print(dis)
ans = [0]*(n-1)
for i in range(n):
    q = deque()
    cnt = 1
    q.append(g[i])
    while q:
        d = []
        while q: 
            d += q.popleft()
        for j in d:
            if i != j and (dis[i][j] == 0 or dis[i][j] > cnt):
                dis[i][j] = cnt
                q.append(g[j])
                ans[cnt-1] += 1
        cnt += 1
for a in ans:
    print(int(a/2))
