N,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
total=0
j=0
ssum=sum(a)

if ssum>=x:
    for i in range(N):
        total+=a[i]
        if total>x:
            break
        j+=1
    print(j)
else:
    print(N-1)
