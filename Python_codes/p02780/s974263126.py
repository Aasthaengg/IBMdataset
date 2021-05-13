n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*n
m=0

for i in range(n):
    b[i]=(a[i]+1)/2

c=sum(b[:k])
m=c
for i in range(n-k):
    c-=b[i]
    c+=b[k+i]
    m=max(m,c)
print(m)