n=int(input())
l=list(map(int,input().split()))
s=sum(l)
c=0
m=10000000000000000
for i in range(n-1):
    c+=l[i]
    d=s-c
    a=abs(d-c)
    m=min(m,a)
print(m)
