N=int(input())
pf={}
m=0
insuu=[0]*(N+1)
p=10**9+7
for i in range(1,N+1):
    m=i
    for j in range(2,int(m**0.5)+1):
        while m%j==0:
            pf[j]=pf.get(j,0)+1
            m//=j
    if m>1:pf[m]=1
    #print(pf)
    keys=list(pf.keys())
    values=list(pf.values())
    pf={}
    for j in range(len(keys)):
        insuu[keys[j]]=insuu[keys[j]]+values[j]
    #print(insuu)
    #input()
    #print(l)	#これでlistになった
ans=1
for i in range(N+1):
    if insuu[i]>0:
        ans=(ans*(insuu[i]+1))%p
print(ans%p)