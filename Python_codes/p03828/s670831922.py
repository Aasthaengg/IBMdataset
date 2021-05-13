n=int(input())
#w,h,x,y,r=map(int,input().split())
#al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
#素因数分解した結果を2次元配列にして返す
def prime_factorize(n):
    n_origin=n+0
    primelist=[]
    a=2
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
dic={}
for i in range(1,n+1):
    pfs=prime_factorize(i)
    for pf in pfs:
        dic[pf[0]]=dic.get(pf[0],0)+pf[1]
#print(dic)
ans=1
mod=10**9+7
for v in dic.values():
    ans=(ans*(v+1))%mod
print(ans)

