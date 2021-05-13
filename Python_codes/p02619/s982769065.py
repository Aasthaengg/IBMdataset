D=int(input())
C=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(D)]
T=[int(input()) for i in range(D)]
result=0
last=[0 for i in range(26)]

for i in range(D):
    t=T[i]-1
    last[t]=-1
    result+=S[i][t]
    for j in range(26):
        last[j]+=1
        result-=last[j]*C[j]
    print(result)