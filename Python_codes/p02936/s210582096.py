N,Q=map(int,input().split())
L=[[]for i in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    L[a].append(b)
    L[b].append(a)
#print(L)

P=[[0,0] for i in range(N+1)]
for i in range(Q):
    p,x=map(int,input().split())
    P[p][1]+=x
#print(P)
P[1][0]=1
A=[]
for i in L[1]:
    A.append([1,i])
    P[i][0]=1
    P[i][1]+=P[1][1]
#print(A)
#print(P)
for i in range(10**7):
    if i==len(A):
        break
    s,g=A[i]
    for j in L[g]:
        if P[j][0]==0:
            P[j][0]=g
            P[j][1]+=P[g][1]
            A.append([g,j])
    #print(A)
ans=[]
for i in range(1,N+1):
    ans.append(P[i][1])
print(*ans)