n=int(input())

#素因数分解した結果を2次元配列にして返す
def prime_factorize(n):
    primelist=[]
    a=2
    n_origin=n
    while a*a<=n_origin:
        if n%a!=0:
            a+=1
            continue
        ex=0
        while n%a==0:
            ex+=1
            n=n//a
        primelist.append([a,ex])
        a+=1
    if n!=1:
        primelist.append([n,1])
    return primelist
mod=10**9+7
dic={}
ans=1
for i in range(2,n+1):
    pfs=prime_factorize(i)
    for j in range(len(pfs)):
        dic[pfs[j][0]]=dic.get(pfs[j][0],0)+pfs[j][1]
for v in dic.values():
    ans=(ans*(v+1))%mod
print(ans)