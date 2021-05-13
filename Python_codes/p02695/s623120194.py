N,M,Q=map(int,input().split())
from copy import copy
A=[]
def DFS(n,s):
    if len(s)==n:
        A.append(copy(s))
        return
    ss=s[-1]
    for i in range(ss,M+1):
        s.append(i)
        DFS(n,s)
        s.pop()

DFS(N,[1])

q=[]
for i in range(Q):
    a,b,c,d=map(int,input().split())
    q.append([a,b,c,d])

L=len(A)
ans=0
for i in range(L):

    point=0
    for j in range(Q):
        a,b,c,d=q[j]
        if A[i][b-1]-A[i][a-1]==c:
            point+=d
    ans=max(ans,point)
print(ans)


