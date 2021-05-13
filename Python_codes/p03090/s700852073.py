n=int(input())
if n%2==0:
    print(n*(n-2)//2)
else:
    print((n-1)*(n-3)//2+n-1)
    for i in range(n-1):
        print(i+1,n)
    n-=1
for i in range(1,n):
    for j in range(i+1,n+1):
        if i+j!=1+n:
            print(i,j)