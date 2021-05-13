s=input()
n=len(s)
ten=[1]
p=1
mod=10**9+7
for i in range(n-1):
    p*=10
    p%=13
    ten.append(p)
ten=ten[::-1]
dp=[0]*13
dp[0]=1
for t,c in zip(ten,s):
    newdp=[0]*13
    if c!='?':
        c=t*int(c)%13
        for i in range(13):
            newdp[(i+c)%13]=dp[i]
    else:
        for c in range(10):
            c*=t
            for i in range(13):
                newdp[(i+c)%13]+=dp[i]
                newdp[(i+c)%13]%=mod
    dp=newdp

print(newdp[5])