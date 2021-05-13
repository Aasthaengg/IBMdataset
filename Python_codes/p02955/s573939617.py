n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=1
A=sum(a)
l=[]
for i in range(1,int(A**(1/2))+1):
    if A%i!=0:continue
    l.append(i)
    if  A// i != i:
        l.append(A // i)
for i in l:
    x=[0]*n
    for j in range(n):
        x[j]=a[j]%i
    s=sum(x)
    l=0
    x.sort(reverse=True)
    for j in range(n):
        if s<=k and l<=k:
            if (s-l)%i==0:
                if i>cnt:
                    cnt=i
                break
        l+=i-x[j]
        s-=x[j]

print(cnt)