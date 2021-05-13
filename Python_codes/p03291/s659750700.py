s=input()
n=len(s)
q=s.count('?')

mod=10**9+7

target='ABC'
ans=0
for i in range(2**3):
    bdp=[1]*(n+1)
    cnt=0
    for j in range(2,-1,-1):
        if (i>>j)&1==1:
            c='?'
            cnt+=1
        else:
            c=target[j]
        
        cdp=[0]*(n+1)
        for k in range(n):
            if s[k]==c:
                cdp[k]=bdp[k+1]
        
        for k in range(n,0,-1):
            cdp[k-1]+=cdp[k]
            cdp[k-1]%=mod
        
        bdp=cdp
    
    if q>=cnt:
        ans+=bdp[0]*pow(3,q-cnt,mod)
        ans%=mod

print(ans)