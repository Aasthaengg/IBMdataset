q=int(input())
l=[]
r=[]
for i in range(q):
    lr=list(map(int,input().split()))
    l.append(lr[0])
    r.append(lr[1])
n=sorted(r,reverse=True)[0]
prime=[True]*(n+1)
prime[0]=False
prime[1]=False
for i in range(2,int(n**(0.5))+1):
    if prime[i]:
        for j in range(i*2,n,i):
            prime[j]=False
a=[0]*(n+1)
for i in range(n+1):
    if i%2==0:
        continue
    if prime[i] and prime[(i+1)//2]:
        a[i]=1
s=[0]*(n+2)
for i in range(n+1):
    s[i+1]=s[i]+a[i]
for i in range(q):
        print(s[r[i]+1]-s[l[i]])