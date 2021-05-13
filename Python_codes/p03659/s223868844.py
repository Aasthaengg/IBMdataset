n=int(input())
a=list(map(int,input().split()))

f=0
b=sum(a)
m=abs(a[0]-sum(a[1:]))
for i in range(n-1):
    f+=a[i]
    b-=a[i]
    m=min(m,abs(f-b))
print(m)