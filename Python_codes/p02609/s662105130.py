def popcount(x):
    if x in memo:
        return memo[x]
    res=0
    while(x>0):
        if x&1:
            res+=1
        x//=2
    memo[x]=res
    return res
memo={}

N=int(input())
X=input()[::-1]
c=X.count('1')
count=[0]*(c+2)
for i in range(c+2):
    x=i
    cnt=0
    while(x>0):
        x=x%popcount(x)
        cnt+=1
    count[i]=cnt

if X[0]=='0':
    summ,sumn,sump=0,0,0
else:
    summ,sumn,sump=1,1,1
bitm,bitn,bitp=[0]*N,[0]*N,[0]*N
bitm[0],bitn[0],bitp[0]=1,1,1
for i in range(1,N):
    if c>1:
        bitm[i]=bitm[i-1]*2%(c-1)
    bitn[i]=bitn[i-1]*2%c
    bitp[i]=bitp[i-1]*2%(c+1)
    if X[i]=='1':
        if c>1:
            summ=(summ+bitm[i])%(c-1)
        sumn=(sumn+bitn[i])%c
        sump=(sump+bitp[i])%(c+1)
ans=[]
for i in range(N):
    if X[i]=='0':
        x=(sump+bitp[i])%(c+1)
        ans.append(count[x]+1)
    else:
        if c==1:
            ans.append(0)
        else:
            x=(summ-bitm[i]+c-1)%(c-1)
            ans.append(count[x]+1)
print(*ans[::-1],sep='\n')