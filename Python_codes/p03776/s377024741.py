from collections import Counter

def nCr(n,r):
    return fac[n]//fac[r]//fac[n-r]

N,A,B=map(int,input().split())
v=sorted(map(int,input().split()),reverse=True)
fac=[1]
for i in range(N):
    fac.append(fac[-1]*(i+1))
print(sum(v[:A])/A)
c=Counter(v)
if v[0]==v[A-1]:
    Cnt=c[v[0]]
    res=0
    for i in range(A,B+1):
        res+=nCr(Cnt,i)
    print(res)
else:
    All=c[v[A-1]]
    M=v[:A].count(v[A-1])
    print(nCr(All,M))