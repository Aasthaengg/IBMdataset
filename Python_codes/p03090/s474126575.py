n=int(input())

if n%2==0:
    m=n*(n-1)//2-n//2
    print(m)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j==n+1:
                continue
            print('{} {}'.format(i,j))
else:
    m=n*(n-1)//2-(n-1)//2
    print(m)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j==n:
                continue
            print('{} {}'.format(i,j))