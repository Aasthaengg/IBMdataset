#A,G,C,T=0,1,2,3
#AGC,ACG,GACを含まない
#A?GC,AG?Cを含まない
import copy

n=int(input())
A=[[1,1,1,1],[1,1,0,1],[1,0,1,1],[1,1,1,1]] #3文字前がAのとき
B=[[3,3,2,3],[3,3,3,3],[3,3,3,3],[3,3,3,3]] #それ以外
mod=10**9+7

for _ in range(n-3):
    nA=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    nB=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4): #付け足す文字
            if j!=2: #3文字前がAで、Cを足さないとき
                if not (i==2 and j==1): #ACG
                    nA[i][j]+=A[0][i]
                nB[i][j]+=A[1][i]
                nB[i][j]+=A[2][i]
                nB[i][j]+=A[3][i]
            else: #Cを足すとき
                if i!=1: #A?GC
                    nA[i][j]+=A[0][i]
                    #nB[i][j]+=A[1][i] #AG?C
                    nB[i][j]+=A[2][i]
                    nB[i][j]+=A[3][i]
            
            if not i*j==2: #AGC,ACG
                nA[i][j]+=B[0][i]
            if not (i==0 and j==2): #GAC
                nB[i][j]+=B[1][i]
            nB[i][j]+=B[2][i]
            nB[i][j]+=B[3][i]
    for a in nA:
        for i in range(4):
            a[i]%=mod
    for b in nB:
        for i in range(4):
            b[i]%=mod
    A=copy.copy(nA)
    B=copy.copy(nB)
    
ans=0
for a in A:
    ans+=sum(a)%mod
for b in B:
    ans+=sum(b)%mod 
print(ans%mod)