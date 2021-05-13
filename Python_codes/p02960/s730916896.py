
import sys

s=input()

n=[0]*6
q=[0]*6
j=[1,10,9,12,3,4,1]
lens=len(s)
for i in range(lens):
    i6=i%6
    if s[lens-1-i]=="?":
        q[i6]+=1
    else:
        n[i6]+=int(s[lens-1-i])

mod=10**9+7
    
nsum=0
for i in range(6):
    nsum+=(n[i]*j[i])%13
nsum=(5-nsum)%13

if q==[0]*6:
    if nsum==0:
        print(1)
    else:
        print(0)
    sys.exit()
        
cc2=[[-1]*13 for i in range(6)]

for i6 in range(6):
    for i in range(10):
        iii=(i*10**i6)%13
        cc2[i6][i]=iii

#dp=[[0]*13 for i in range(80)]
dpm=[0]*13
dpn=[0]*13
icnt=-1
for i6 in range(6):
    for i in range(q[i6]):
        dpn=[0]*13
        icnt+=1
        if icnt==0:
            for j in range(10):
                jj=(j*10**i6)%13
#                dp[icnt][jj]=1            
#                dpn[jj]=1
                dpm[jj]=1
            continue
        for mi in range(13):
            for j in range(10):
#                ccir=(mi-(j*(10**i6))%13)%13
                ccir=(mi-cc2[i6][j])%13
#                dp[icnt][mi]=(dp[icnt][mi]+dp[icnt-1][ccir])%mod
                dpn[mi]=(dpn[mi]+dpm[ccir])%mod
        dpm=dpn.copy()  
#    print(icnt,dp[icnt])

#print(dp[icnt][nsum]%mod)
print(dpm[nsum]%mod)
            
