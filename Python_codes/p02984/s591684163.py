n=int(input())
a=list(map(int,input().split()))

x=[0]*n
s=sum(a)
x0_total=0
for i in range(1,n-1,2):
    x0_total+=a[i]
x[0]=s-x0_total*2

for i in range(1,n):
    if i==n-1:
        x[n-1]=2*a[n-1]-x[0]
    else:
        x[i]=2*a[i-1]-x[i-1]

print(' '.join(map(str,x)))