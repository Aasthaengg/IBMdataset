n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n):
    if n%2:
        if i==n//2:
            b[i]=a[0]
        elif i<n//2:
            b[i]=a[n-i*2-1]
        else:
            b[i]=a[(i-n//2)*2-1]
    else:
        if i<n//2:
            b[i]=a[n-i*2-1]
        else:
            b[i]=a[(i-n//2)*2]
print(' '.join(map(str,b)))