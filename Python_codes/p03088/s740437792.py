#we like agc
n=int(input())
import itertools
P=list(itertools.product('ACGT', repeat=3))
mod=10**9+7
use=[] 
for some in P:
    some=list(some)
    K="".join(some)
    use.append(K)
dp=[{some:0 for some in use}for k in range(n+1)]
for some in use:
    if some!="AGC" and some!="ACG" and some!="GAC":
        dp[3][some]=1

D=["A","C","G","T"]
for i in range(4,n+1):
    for some in use:
        #some=AAA,AAC,AAG,,,,,,,,TTT
        for j in range(4):
            S=list(some+D[j])
            if (S[0]=="A" and S[2]=="G" and S[3]=="C")  or (S[1]=="G" and S[2]=="A "and S[3]=="C") or (S[0]=="A" and S[1]=="G" and S[3]=="C"):
                pass
            else:
                if some!="AGC" and some!="ACG" and some!="GAC":
                    dp[i]["".join(S[1:])]+=dp[i-1][some]
                    dp[i]["".join(S[1:])]=dp[i]["".join(S[1:])]%mod
ans=0
for some in use:
    if some!="AGC" and some!="ACG" and some!="GAC":
        ans+=dp[n][some]
print(ans%mod)