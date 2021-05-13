def nCr(n,r):
    return fac[n]//fac[r]//fac[n-r]

N,A,B=map(int,input().split())
v=sorted(map(int,input().split()),reverse=True)

fac=[1]
for i in range(N):
    fac.append(fac[-1]*(i+1))

print(sum(v[:A])/A)

Cnt=v.count(v[A-1])
res=0

if v[0]==v[A-1]:
    for i in range(A,B+1):
        res+=nCr(Cnt,i)

else:
    M=v[:A].count(v[A-1])
    res=nCr(Cnt,M)

print(res)