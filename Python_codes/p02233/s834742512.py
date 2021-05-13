n=int(input())
a=list(range(n+1))
a[0]=1
i=2
while i<=n:
    a[i]=a[i-1]+a[i-2]
    i+=1
print(a[n])
