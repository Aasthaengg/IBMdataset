L=input()
L=L+"0"
L=L[::-1]
pow3=[0 for i in range(110000)]
pow3[0]=1
mod=10**9+7
for i in range(1,100010):
    pow3[i]=pow3[i-1]*3%mod
#pow3[i]=3**iをmodで割ったあまり
a=1
for i in range(len(L)):
    if L[i]=="1":
        a=(a*2+pow3[i-1])%mod
print(a%mod)