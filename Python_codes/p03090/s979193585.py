n=int(input())
if n%2:
    print(2*(n//2)**2)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j==n:continue
            print(i,j,sep=" ")
else:
    s=n//2
    print(2*(s-1)*s)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j==n+1 :continue
            print(i,j,sep=" ")