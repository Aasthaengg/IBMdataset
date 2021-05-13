N=int(input())
A=list(map(int,input().split()))
S=0
B=[0]*(10**5+1)
for i in A:
    S+=i
    B[i]+=1  #Bは要素数管理
Q=int(input())
C=[list(map(int,input().split())) for i in range(Q)]
for i in range(Q):
    S=S+(C[i][1]-C[i][0])*B[C[i][0]]
    B[C[i][1]]=B[C[i][0]]+B[C[i][1]]
    B[C[i][0]]=0
    print(S)