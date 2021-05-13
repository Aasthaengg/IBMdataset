n=int(input())
b=list(map(int,input().split()))
a=[0]*n
for i in range(n-2):
    if b[i]<=b[i+1]:
        a[i+1]=b[i]
    else:
        a[i+1]=b[i+1]
a[0]=b[0]
a[n-1]=b[n-2]
A=0
for i in range(n):
    A+=a[i]
print(A)