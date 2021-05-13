import sys
input=sys.stdin.readline
N,K=map(int,input().split())
P=[0 for i in range(N+1)]
C=[0 for i in range(N+1)]

L=[[]for i in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    L[a].append((a,b))
    L[b].append((b,a))
    
P[1]=-1
Q=L[1]
#print(Q)
#print(L)
for i in range(N-1):
    #print(i,Q)
    if P[Q[i][1]]==0:
        P[Q[i][1]]=Q[i][0]
        C[Q[i][0]]+=1
        for j in L[Q[i][1]]:
            if P[j[1]]==0:
                Q.append(j)
    #print(i)
#print(P,C,Q)
mod=10**9+7
ans=K
for i in range(C[1]):
    ans*=(K-i-1)
    ans%=mod
    
#print(ans)
ANS=[0 for i in range(N+1)]
ANS[1]=ans
for i in range(2,N+1):
    if C[i]!=0:
        for j in range(C[i]):
            ans*=(K-j-2)
            #print(i,j)
            ans%=mod
            ANS[i]=ans
#print(ANS)
print(ans)