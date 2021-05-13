L=input()
#L 最大100000桁
N=len(L)
p=10**9+7
#iけた目が１
#1~N-1まで
ans1=0
for i in range(1,N):
    now=(2*pow(3, (i-1), p))%p
    ans1+=now
    ans1%=p

#Nけた目が１
dp=[0]*N
equals=[0]*N
dp[0]=0
equals[0]=2
for i in range(1,N):
    if L[i]=="0":
        equals[i]=equals[i-1]
        dp[i]=(dp[i-1]*3)%p
    else:
        equals[i]=(equals[i-1]*2)%p
        dp[i]=((dp[i-1]*3)+equals[i-1])%p

print((1+ans1+dp[-1]+equals[-1])%p)
#print(dp, equals)