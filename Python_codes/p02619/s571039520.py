def 一日経過(n):
    return n+1
    
D=int(input())
C=list(map(int,input().split()))
S=[]
Ans=0
last=[0 for i in range(26)]
for i in range(D):
    s=list(map(int,input().split()))
    S.append(s)
for i in range(D):
    last=list(map(一日経過,last))
    t=int(input())-1
    last[t]=0
    Ans+=S[i][t]
    for j in range(26):
        Ans-=C[j]*last[j]
    print(Ans)