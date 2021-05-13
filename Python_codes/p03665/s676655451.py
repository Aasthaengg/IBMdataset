n,p=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=a[i]%2
one=sum(a)
zero=n-one
if p==1 and one==0:
    print(0)
    exit()
if p==0 and one==0:
    print(2**n)
    exit()
print(2**(n-1))