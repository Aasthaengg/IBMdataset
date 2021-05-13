n,m=map(int,input().split())
if n%2==1:
    for i in range(m):
        print(i+1,n-i)
else:
    for i in range(m):
        if i%2==0:
            print(i//2+1,n-i//2)
        else:
            print(n//2-i//2-1,n//2+i//2+1)