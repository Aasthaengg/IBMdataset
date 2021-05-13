m,k=map(int,input().split())
a=['']*(2**(m+1))
if k==0:
    for i in range(2**m):
        for j in range(2):
            a[2*i+j]=str(i)
else:
    xor=0
    for i in range(2**m):
        if i<k:
            a[i]=str(i)
            xor^=i
        elif i>k:
            a[i-1]=str(i)
            xor^=i
    
    if xor!=k:
        print(-1)
        exit(0)
    
    a[2**m-1]=str(k)
    for i in range(2**m-1,-1,-1):
        if i>k:
            a[2**(m+1)-i-1]=str(i)
        elif i<k:
            a[2**(m+1)-i-2]=str(i)
    
    a[2**(m+1)-1]=str(k)


print(' '.join(a))