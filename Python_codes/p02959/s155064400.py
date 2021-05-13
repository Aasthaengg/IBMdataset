n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

goukei=sum(a)

for i in range(len(b)):
    if b[i]>a[i]:
        a[i+1]=a[i+1]+a[i]-b[i]
        a[i]=0
        if a[i+1]<0:
            a[i+1]=0
    else:
        a[i]=a[i]-b[i]
print(goukei-sum(a))