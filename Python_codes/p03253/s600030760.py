from collections import defaultdict
n,m=map(int,input().split())
mod=10**9+7
kaidan=[1]*(2*10**5+1)
gyaku=[1]*(2*10**5+1)

for i in range(1, 2*10**5):
    kaidan[i]=i*kaidan[i-1] % mod
    gyaku[i]=pow(kaidan[i],mod-2,mod)
def comb(a,b):
    if a>0 and b>0 and a-b>0:
        return (kaidan[a] * gyaku[b]*gyaku[a-b])%mod
    elif a==0 or b==0 or a-b==0:
        return 1
    else:
        return 0
def fctr1(n): 
    f=[]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append([i,c])
            c=0
    if n!=1:
        f.append([n,1])
    return f
# soin=defaultdict(int)
# while m>=2:
#     for i in range(2,int(n**.5)+5):
#         while m%i==0 and m!=0:
#             m//=i
#             soin[i]+=1
#             if m==1:
#                 break
     
L=list(fctr1(m))
ans=1
for a,l in L:
    ans*=comb(l+n-1,l)
    ans%=mod
print(ans)