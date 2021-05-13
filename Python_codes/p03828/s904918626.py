n=int(input())
q=10**9+7

x=[-1]*(n+1) #2以上の自然数に対して最小の素因数を表す
x[0]=0
x[1]=1
i=2
prime=[]
while i<=n:
    if x[i]==-1:
        x[i]=i
        prime.append(i)
    for j in prime:
        if i*j>n or j>x[i]:break
        x[j*i]=j
    i+=1

d=[0]*(n+1)
for i in range(1,n+1):
    while x[i]!=1:
        p=x[i]
        d[p]+=1
        i=i//p

ans=1

for i in range(n+1):
    ans=ans*(d[i]+1)%q
print(ans%q)


