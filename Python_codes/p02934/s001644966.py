def gyaku(x):
    return 1/x

n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=gyaku(a[i])

x=sum(a)
print(gyaku(x))