s=int(input())

mod=10**9+7

def c(a,p):
    x=1
    for y in range(p+1,a+1):
        x=(x*y)%mod
    z=1
    for y in range(1,a-p+1):
        z=(z*y)%mod
#    print("x:",x,"z:",z,(x* pow(z, mod-2,mod))%mod)
    return (x* pow(z, mod-2,mod))%mod    

ss=s//3
icnt=0
for sss in range(1,ss+1):
    r=s-3*sss
#    print("icnt:",icnt,"sss:",sss-1,"r:",r,c(sss-1+r,sss))
    icnt=(icnt+c(sss+r-1,sss-1))%mod

print(icnt)
