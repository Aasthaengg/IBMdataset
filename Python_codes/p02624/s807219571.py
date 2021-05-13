n=int(input())

x=[-1]*(10**7+5)
x[0]=0
x[1]=1
i=2
prime=[]
while i<=10**7+1:

    if x[i]==-1:
        x[i]=i
        prime.append(i)

    for j in prime:
        if i*j>10**7+1 or j>x[i]:break
        x[j*i]=j
    i+=1



def f(k):
    if k==1:
        return 1

    z=[]
    p=x[k]
    m=1
    ans=1
    while k>=2:
        k=k//p
        if p==x[k]:
            m+=1
        else:
            z.append(m)
            m=1
            p=x[k]

    for i in range(len(z)):
        ans*=z[i]+1
    return ans
ans=0
for i in range(1,n+1):
    #print(i,f(i))
    ans += i*f(i)

print(ans)