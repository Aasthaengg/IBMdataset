from collections import deque
def tsort():
    que=deque([i for i,c in enumerate(In) if c==0])
    l=[]
    while que:
        v=que.popleft()
        l.append(v)
        for nv in G[v]:
            In[nv]-=1
            if In[nv]==0:
                que.append(nv)
    if len(l)!=P:
        print(-1)
        exit()
    return l
    
def setID():
    t=0
    ID=[[None]*N for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            ID[i][j]=t
            t+=1
    for i in range(N):
        for j in range(N-1):
            a,b=i,A[i][j]
            if(a>b):
                a,b=b,a
            A[i][j]=ID[a][b]
    return t
N=int(input())
A=[list(map(lambda x:int(x)-1,input().split())) for i in range(N)]
P=setID()
In=[0]*P
G=[[] for i in range(P)]
for i in range(N):
    for j in range(N-2):
        G[A[i][j]].append(A[i][j+1])
        In[A[i][j+1]]+=1
srted=tsort()
dp=[1]*P
for v in srted:
    for nv in G[v]:
        dp[nv]=max(dp[nv],dp[v]+1)
print(max(dp))