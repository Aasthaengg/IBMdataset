N,M,K=map(int,input().split())

mod=998244353

ans=0

comb=[1]
for i in range(K):
    comb_temp=comb[i]*(N-1-i)*pow(i+1,-1,mod)
    comb_temp%=mod
    comb.append(comb_temp)

for k in range(K+1):
    ans_temp=M*(comb[k])*pow(M-1,N-1-k,mod)
    ans+=ans_temp
    ans%=mod

print(ans)