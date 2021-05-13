S=input()
lens=len(S)
mod=10**9+7
cnt=[0,0,0,1]
for s in S:
    if s=="A":
        cnt[0]=(cnt[0]+cnt[3])%mod
    elif s=="B":
        cnt[1]=(cnt[0]+cnt[1])%mod
    elif s=="C":
        cnt[2]=(cnt[1]+cnt[2])%mod
    else:
        cnt[2]=(cnt[1]+3*cnt[2])%mod
        cnt[1]=(cnt[0]+3*cnt[1])%mod
        cnt[0]=(3*cnt[0]+cnt[3])%mod
        cnt[3]=cnt[3]*3%mod
print(cnt[2]%mod)