n=int(input())
mod=10**9+7
#A=0,C=1,G=2,T=3
table=[1]*(64)
data=[[] for i in range(64)]
for i in range(64):
    z=i
    num=""
    for j in range(3):
        if i//(4**(2-j))==1:
            num+="1"
            i%=(4**(2-j))
        elif i//(4**(2-j))==2:
            num+="2"
            i%=(4**(2-j))*2
        elif i//(4**(2-j))==3:
            num+="3"
            i%=(4**(2-j))*3
        else:
            num+="0"
    for j in range(4):
        a=num+str(j)
        b=a[1]+a[0]+a[2]+a[3]
        c=a[0]+a[2]+a[1]+a[3]
        d=a[0]+a[1]+a[3]+a[2]
        if "021" in a or "021" in b or "021" in c or "021" in d:
            continue
        else:
            data[z].append(16*int(a[1])+4*int(a[2])+int(a[3]))
table[6]=0
table[9]=0
table[33]=0
for i in range(n-3):
    h=[0]*64
    for j in range(64):
        for u in data[j]:
            h[u]=(h[u]+table[j])%mod
    table=h
ans=0
for i in range(64):
    ans=(ans+table[i])%mod
print(ans)