n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.append(0)

ans = sum(a)

if a[0]<b[0]:
    b[0]-=a[0]
    a[0]=0
else:
    a[0]-=b[0]
    b[0]=0
    
for i in range(1,n+1):
    if a[i]<b[i-1]+b[i]:
        if a[i]>b[i-1]:
            b[i] -= a[i] - b[i-1]
            b[i-1] =0
        else:
            b[i-1] -= a[i]
        a[i]=0
    else:
        a[i] -= b[i-1]+b[i]
        b[i]=0
print(ans-sum(a))
