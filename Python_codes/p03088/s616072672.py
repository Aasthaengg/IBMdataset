N=int(input())

ch=['A','G','C','T']
ban3=['AGC','GAC','ACG']
ban4=['ATGC','AGGC','AGTC']
dp=[{},{}]

mod=10**9+7

for i in range(4**3):
    s=''
    for j in range(3):
        s+=ch[(i>>(j*2))%4]
    
    if s in ban3:
        dp[0][s]=0
    else:
        dp[0][s]=1
    
    dp[1][s]=0

cnt=0

while N>3:
    for k in dp[(cnt+1)%2]:
        dp[(cnt+1)%2][k]=0
    
    for k,v in dp[cnt].items():
        for c in ch:
            nk=k+c

            if nk in ban4:
                continue

            if nk[1:] in ban3:
                continue

            dp[(cnt+1)%2][nk[1:]]+=dp[cnt][nk[:3]]
            dp[(cnt+1)%2][nk[1:]]%=mod
            
    N-=1
    cnt=(cnt+1)%2

print(sum(dp[cnt].values())%mod)