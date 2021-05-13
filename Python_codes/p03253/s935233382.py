N,M=map(int,input().split())

def factorization(n):#次数だけ
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(cnt)

    if temp!=1:
        arr.append(1)

    if arr==[]:
        arr.append(0)

    return arr
     
p=factorization(M)#素因数分解して次数を調べる

    
def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return (fact[n] * factinv[r] * factinv[n-r])%mod

mod=10**9 + 7
fact=[1,1]
factinv=[1,1]
inv=[0,1]
 
N2=N+max(p)    

for i in range(2, N2 + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
    

        
ans=1
for i in range(len(p)):
    ans*=cmb(p[i]+N-1,p[i],mod)
    ans%=mod

print(ans)


