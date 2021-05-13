S=input()
l=len(S)
pow2=[1]
pow3=[1]
mod=10**9+7

for i in range(l+10):
    pow2.append(pow2[-1]*2%mod)
    pow3.append(pow3[-1]*3%mod)
    
if l==1:
    if S=="0":
        print(1)
    else:
        print(3)

else:
    ans=pow3[l-1]
    cnt=1 #現在の桁とその左側の1の数
    for i in range(l-1):
        if i==l-2:
            if S[i+1]=="1":
                ans+=pow2[cnt]*3%mod
            else:
                ans+=pow2[cnt]%mod
        else:
            if S[i+1]=="1":
                ans+=pow2[cnt]*pow3[l-i-2]%mod
                cnt+=1                                                  
    print(ans%mod)