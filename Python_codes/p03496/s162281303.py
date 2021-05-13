
n = int(input())
a = list(map(int,input().split()))
m = min(a)
M = max(a)
mi = a.index(m)
Mi = a.index(M)
if all(a[i]<0 for i in range(n)):
    print(n-1)
    for i in range(n-2,-1,-1):
        print(i+2,i+1)
elif all(a[i]>0 for i in range(n)):
    print(n-1)
    for i in range(0,n-1):
        print(i+1,i+2)
else:
    print(2*n-1)
    if abs(M)>=abs(m):
        for i in range(0,n):
            print(Mi+1,i+1)
        for i in range(0,n-1):
            print(i+1,i+2)
    else:
        for i in range(0,n):
            print(mi+1,i+1)
        for i in range(n-2,-1,-1):
            print(i+2,i+1)