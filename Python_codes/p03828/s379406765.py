N = int(input())
p = 10**9+7
T = [0]*(1001)
for m in range(2,N+1):
    pf={}
    for i in range(2,int(m**0.5)+1):
        while m%i==0:
            pf[i]=pf.get(i,0)+1
            m//=i
    if m>1:pf[m]=1
    for key in pf.keys():
        T[key] += pf[key]
out = 1
for i in range(1001):
    out = out*(T[i]+1)%p
print(out)