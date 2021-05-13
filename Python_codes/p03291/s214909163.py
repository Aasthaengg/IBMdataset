mod=10**9+7
S=input()
N=len(S)
Acnt=[[0,0] for i in range(N+2)]
Ccnt=[[0,0] for i in range(N+2)]
for i in range(N):
    Acnt[i+1]=Acnt[i].copy()
    Ccnt[-i-2]=Ccnt[-i-1].copy()
    if S[i]=="A":
        Acnt[i+1][0]+=1
    if S[i]=="?":
        Acnt[i+1][1]+=1
    if S[-i-1]=="C":
        Ccnt[-i-2][0]+=1
    if S[-i-1]=="?":
        Ccnt[-i-2][1]+=1
Acnt[N+1]=Acnt[N]
Ccnt[-N-2]=Ccnt[-N-1]
ans=0
ruijo=[1]*(N+1)
for i in range(N):
    ruijo[i+1]=ruijo[i]*3%mod
ruijo.append(0)
for i in range(N):
    if S[i]=="B" or S[i]=="?":
        a,b,c,d=0,0,0,0
        a=Acnt[i][0]*Ccnt[i+2][0]*ruijo[Acnt[i][1]+Ccnt[i+2][1]]%mod
        if Ccnt[i+2][1]>0:
            b=Acnt[i][0]*Ccnt[i+2][1]*ruijo[Acnt[i][1]+Ccnt[i+2][1]-1]%mod
        if Acnt[i][1]>0:
            c=Acnt[i][1]*Ccnt[i+2][0]*ruijo[Acnt[i][1]+Ccnt[i+2][1]-1]%mod
        if Acnt[i][1]>0 and Ccnt[i+2][1]>0:
            d=Acnt[i][1]*Ccnt[i+2][1]*ruijo[Acnt[i][1]+Ccnt[i+2][1]-2]%mod
        ans=(ans+a+b+c+d)%mod
print(ans)