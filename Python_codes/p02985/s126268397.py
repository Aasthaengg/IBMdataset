import sys
#階乗
mod=10**9+7
table=[1]*(10**5+100)
for i in range(2,10**5+100):
    table[i]=(table[i-1]*i)%mod
    
#cmb
g1=[1,1]
g2=[1,1]
for i in range(2,10**5+100):
    num_1=g1[-1]*i%mod
    g1.append(num_1)
    g2.append(pow(num_1,mod-2,mod))  
def cmb(n,r,MOD):
    if n<r or n<=0:
        return 0
    else:
        return g1[n]*g2[r]*g2[n-r]%MOD
    
#dfsで進んでいき、3回目以降は親とその親以外の色、kー2通りから考える。
n,k=map(int,input().split())
data=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
if k==2:
    if n<=2:
        print(2)
    else:
        print(0)
    sys.exit()
if k==1:
    if n==1:
        print(1)
    else:
        print(0)
    sys.exit()
flag=[0]*(n+1)
ans=1
ans=cmb(k,len(data[1])+1,mod)*table[len(data[1])+1]%mod
que=data[1]
flag[1]=1
for u in data[1]:
    flag[u]=1
while que:
    h=[]
    for u in que:
        count=0
        for v in data[u]:
            if flag[v]==0:
                flag[v]=1
                h.append(v)
                count+=1
        ans=(ans*cmb(k-2,count,mod)*table[count])%mod
    que=h
print(ans)