n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    if b[i]<=a[i]:
        s+=b[i]
    else:
        s+=a[i]
        c=a[i+1]
        a[i+1]+=a[i]-b[i]
        if a[i+1]<0:
            a[i+1]=0
            s+=c
        else:
            s+=b[i]-a[i]
print(s)