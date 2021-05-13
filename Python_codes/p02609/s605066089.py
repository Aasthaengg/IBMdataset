n=int(input())
x=input()

pcn=x.count('1')
px=int(x,2)%(pcn+1)
mx=int(x,2)%(pcn-1) if pcn>1 else 0
p2=[0]*n
m2=[0]*n

for i in range(n):
    p2[i]=pow(2,n-1-i,pcn+1)
    m2[i]=pow(2,n-1-i,pcn-1) if pcn>1 else 0

for i in range(n):
    p=False if int(x[i])&1 else True
    if pcn==1 and not p:
        print(0)
        continue
    ans=0
    tmp=0
    if(p):
        tmp=(px+p2[i])%(pcn+1)
    else:
        tmp=(mx-m2[i])%(pcn-1)
    ans+=1
    while tmp!=0:
        ipcn=str(bin(tmp)).count('1')
        tmp%=ipcn
        ans+=1
    print(ans)