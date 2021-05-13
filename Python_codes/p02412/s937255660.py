while True:
    n,x = [int(i) for i in input().split()]
    if n==x==0:break
    count=0

    for i in range(1,n+1):
        for j in range(1,n):
            for k in range(1,n-1):
                if i+j+k==x and i>j>k and not i==j==k:
                    count += 1
    print(count)