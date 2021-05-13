n=int(input())
if n%2==0:
    print((n**2-2*n)//2)
    for i in range(1,n):
        for j in range(i+1,n+1):
            if j!=n-i+1:
                print(i,j)
else:
    print((n**2-2*n+1)//2)
    for i in range(1,n):
        for j in range(i+1,n+1):
            if j!=n-i:
                print(i,j)