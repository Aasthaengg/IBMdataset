MOD=1000000007
N=int(input())
S=[input() for _ in range(2)]
i=0
ans=1
flag=True
if S[0][0]==S[1][0]:
    ans=3
    i+=1
else:
    ans=6
    i+=2
    flag=False
while i<N:
    if S[0][i]==S[1][i]:
        if flag==True:
            ans*=2
            ans%=MOD
        i+=1
        flag=True
    else:
        if flag:
            ans*=2
        else:
            ans*=3
        ans%=MOD
        i+=2
        flag=False
print(ans)
