N,M,Q=map(int,input().split())
from copy import copy
stack=[[1]]
A=[]
while stack:
    temp=stack.pop()
    if len(temp)==N:
        A.append(temp)
    else:
        x=temp[-1]
        for i in range(x,M+1):
            temp.append(i)
            stack.append(copy(temp))
            temp.pop()

q=[]
for i in range(Q):
    a,b,c,d=map(int,input().split())
    q.append([a,b,c,d])

L=len(A)
ans=0
for i in range(L):
    point=0
    for j in range(Q):
        if A[i][q[j][1]-1]-A[i][q[j][0]-1]==q[j][2]:
            point+=q[j][3]
    ans=max(ans,point)
print(ans)