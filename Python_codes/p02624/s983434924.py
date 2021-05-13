n=int(input())

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

def f(k):
    z=[]
    if k==1:
        return 1
    p=x[k]
    c=1
    while k>1:
        if p!=x[k//p]:
            z.append(c)
            c=1
        else:
            c+=1

        k=k//p
        p=x[k]

    ans=1
    for i in range(len(z)):
        ans=ans*(z[i]+1)
    return ans
s=0
for i in range(n):
    s+=(i+1)*f(i+1)
print(s)

