n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n,0,-1):
    s=0
    for j in range(1,n+1):
        if j*i<=n:
            s+=b[i*j-1]
        else:
            break
    if s%2!=a[i-1]:
        b[i-1]+=1
c=[]
for i in range(n):
    if b[i]==1:
        c.append(i+1)
m=sum(b)
print(m)
print(*c)