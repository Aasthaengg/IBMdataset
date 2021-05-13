s=input()

mod=10**9+7

ans=[[0]*13 for _ in range(len(s))]

if s[-1]=="?":
    for i in range(10):
        ans[-1][i%13]+=1
else:
    ans[-1][int(s[-1])%13]+=1

#print(ans)

ten=1
for ii in range(1,len(s)):
    ten=(ten*10)%13

    i=len(s)-ii-1
    
    if s[i]!="?":
        tmp=(int(s[i])*ten)%13
        for j in range(13):
            ans[i][(tmp+j)%13]+=(ans[i+1][j])%mod
    else:
        for k in range(10):
            tmp=(k*ten)%13
            for j in range(13):
                ans[i][(tmp+j)%13]+=(ans[i+1][j])%mod

print(ans[0][5]%mod)



