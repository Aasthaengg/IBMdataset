n=int(input())
b=list(map(int,input().split()))
a=[0]*n
for i in range(n):
    if i==0:
        a[i]=b[i]
    elif 0<i<n-1:
        a[i]=min(b[i-1],b[i])
    else:
        a[i]=b[i-1]
print(sum(a))