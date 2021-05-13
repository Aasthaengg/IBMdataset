S=input()
N=len(S)
mod=10**9+7

list_=[[0,0,0,0]]*(N+1)
for cur in range(N,-1,-1):
    for i in range(4):
        if cur==N:
            if i==3:
                list_[N][i]=1
            else:
                list_[N][i]=0
        else:
            if S[cur]=='ABCD'[i]:
                list_[cur][i]=(list_[cur+1][i+1]+list_[cur+1][i])%mod
            elif S[cur]=='?' and i!=3:
                list_[cur][i]=(list_[cur+1][i+1]+3*list_[cur+1][i])%mod
            elif S[cur]=='?':
                list_[cur][i]=3*list_[cur+1][i]%mod
            else:
                list_[cur][i]=list_[cur+1][i]%mod

print(list_[0][0]%mod)