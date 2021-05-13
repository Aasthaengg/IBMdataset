n,m = map(int,input().split( ))

fct = {}

for i in range(2,int(m**(1/2))+10):
    if m%i==0:##合成数で割れることはない
        fct[i]=1
        m//=i
        while m%i==0:
            fct[i]+=1
            m//=i
if m>1:
    fct[m]=1
mod = 10**9+7
def h(a,b):
    res = 1
    for i in range(a+b-1,a-1,-1):
        res *= i
        res %= mod
    for i in range(1,b+1):
        res *= pow(i,mod-2,mod)
        res %= mod
    return res
ans = 1
for p in fct:
    ans *= h(n,fct[p])
    ans%=mod
print(ans)
