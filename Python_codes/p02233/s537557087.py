n=int(input())
if n==0 or n==1:
    print(1)
else:
    a=[]
    a.append(1)
    a.append(1)
    for i in range(2,n+1):
        m=a[i-2]+a[i-1]
        a.append(m)
    print(m)
