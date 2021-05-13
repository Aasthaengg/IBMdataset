N=int(input())
P=list(map(float,input().split()))
C=[[0.00]*(N+1) for i in range(N+1)]
C[0][0]=1.00
for i in range(1,N+1):
    for j in range(0,i+1):
        """
        #print(i-1)
        print(P[i-1])
        print(C[i-1][j-1])
        print(C[i-1][j-1]*P[i-1])
        """
        C[i][j]=float(C[i-1][j-1]*P[i-1])+float(C[i-1][j]*(1-P[i-1]))
        #print(C[i][j])
ans=float(0.00)
for i in range((N-1)//2+1):
    ans+=C[N][i]
ans=float(1.00-ans)
print(ans)
