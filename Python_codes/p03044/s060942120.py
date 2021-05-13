def BFS(x):
    v = deque([x])
    d[x]=0
    
    while v:
        a = v.popleft()
        for num in L[a]:
            if d[num]==-1:
                d[num]= d[a]+dic[(a,num)]
                v.append(num)

from collections import deque
N=int(input())
u=[0]*(N-1)
v=[0]*(N-1)
w=[0]*(N-1)
d=[-1 for _ in range(N)]
dic={}
L=[ [] for _ in range(N)]
for i in range(N-1):
    u[i],v[i],w[i] = map(int,input().split())
    u[i] -=1
    v[i] -=1
    L[u[i]].append(v[i])
    L[v[i]].append(u[i])
    dic[ (u[i],v[i])]=w[i]
    dic[ (v[i],u[i])]=w[i]
    
#print(L)
#print(dic)

BFS(0)
#print(d)
for num in d:
    if num%2==0:
        print(0)
    else:
        print(1)