import sys
input=sys.stdin.readline

a,b,q=map(int,input().split())
A=[]
for i in range(a):
    A.append(int(input()))
B=[]
for i in range(b):
    B.append(int(input()))
Q={}
for i in range(q):
    Q[int(input())]=i
X=sorted(Q)

C=[]
now=0
for i in range(a):
    while now<b and A[i]>=B[now]:
        now+=1
    if now==0:
        C.append(abs(A[i]-B[0]))
    elif now==b:
        C.append(abs(A[i]-B[b-1]))
    else:
        C.append(min(abs(A[i]-B[now-1]),abs(A[i]-B[now])))
D=[]
now=0
for i in range(b):
    while now<a and B[i]>=A[now]:
        now+=1
    if now==0:
        D.append(abs(B[i]-A[0]))
    elif now==a:
        D.append(abs(B[i]-A[a-1]))
    else:
        D.append(min(abs(B[i]-A[now-1]),abs(B[i]-A[now])))

Y=[]
now=0
for i in range(q):
    while now<b and X[i]>=B[now]:
        now+=1
    if now==0:
        Y.append(abs(X[i]-B[0])+D[0])
    elif now==b:
        Y.append(abs(X[i]-B[b-1])+D[b-1])
    else:
        Y.append(min(abs(X[i]-B[now-1])+D[now-1],
                     abs(X[i]-B[now])+D[now]))
Z=[]
now=0
for i in range(q):
    while now<a and X[i]>=A[now]:
        now+=1
    if now==0:
        Z.append(abs(X[i]-A[0])+C[0])
    elif now==a:
        Z.append(abs(X[i]-A[a-1])+C[a-1])
    else:
        Z.append(min(abs(X[i]-A[now-1])+C[now-1],
                     abs(X[i]-A[now])+C[now]))
        
Ans=[0]*q
for i in range(q):
    x=Q[X[i]] #番号
    Ans[x]=min(Y[i],Z[i])
for ans in Ans:
    print(ans)