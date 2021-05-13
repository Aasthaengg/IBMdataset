n=int(input())
v=list(map(int,input().split()))
a=[0]*n
for i in range(n):
    t=0
    for j in range(n):
        if v[i]>v[j]:
            t+=1
    a[t]=v[i]
for i in range(n):
    if a[i]==0:
        a[i]=a[i-1]
m=0
for i in range(1,n):
    m+=a[i]/(2**(n-i))
print(m+(a[0]/(2**(n-1))))