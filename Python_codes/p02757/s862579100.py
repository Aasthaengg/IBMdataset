N,P=map(int,input().split())
S=input()

if 10%P==0:
    ans=0
    for i in range(N):
        if int(S[i])%P==0:
            ans+=(i+1)
    print(ans)
else:
    S=S[::-1]
    D={}
    D[0]=1
    Amari=0
    for i in range(N):
        I=((Amari)+(pow(10,i,P)*int(S[i])))%P
        Amari=I
        if I not in D:
            D[I]=1
        else:
            D[I]+=1
    ans=0
    for k,v in D.items():
        ans+=v*(v-1)//2
    print(ans)
    #print(D)