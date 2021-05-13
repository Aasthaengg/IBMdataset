mod=1e9+7

if __name__ == '__main__':
    L=input()
    N=len(L)
    DP1=[0]*(N)
    DP2=[0]*(N)
    DP1[0]=1
    DP2[0]=2

    for i in range(N-1):
        DP1[i+1]=3*DP1[i]
        if L[i+1]=="1":
            DP1[i+1]+=DP2[i]
            DP2[i+1]=2*DP2[i]
        else:
            DP2[i + 1] = DP2[i]
        DP1[i+1]%=mod
        DP2[i+1]%=mod

    print(int((DP2[N-1]+DP1[N-1])%mod))


