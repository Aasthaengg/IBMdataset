n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

count=0
for i in range(n):
    if b[i]<a[i]:
        count+=b[i]
    else:
        count+=a[i]
        b[i]-=a[i]
        if b[i]<a[i+1]:
            count+=b[i]
            a[i+1]-=b[i]
        else:
            count+=a[i+1]
            a[i+1]=0

print(count)