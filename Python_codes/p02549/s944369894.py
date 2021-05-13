root=[]
n,k = map(int,input().split())
for i in range(k):
    x,y = map(int,input().split())
    root.append([x,y])

toori=[0]*(2*10**5)+[0]*n+[0]*(2*10**5)
toori[2*10**5]=1
cum=[0]*k
for a,i in enumerate (root):
    s=0
    for j in range (i[0],i[1]+1):
        s+=toori[2*10**5+1-j]
    cum[a]=s
aaa=sum(cum)%998244353
toori[2*10**5+1]+=aaa


for now in range(2,n):#nowが今の場所
    hueru=0
    for a,i in enumerate (root):
        hueru+=(toori[2*10**5+now-i[0]] - toori[2*10**5+now-1-i[1]])
    aaa+=hueru
    aaa%=998244353
    toori[2*10**5+now]+=aaa
    toori[2*10**5+now]%=998244353
    


print(toori[2*10**5+n-1]%998244353)