while True:
    (n, x) = [int(i) for i in input().split()]
    if n == x == 0: break
    ans = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            c=x-i-j
            if c>j and c<=n:
                ans+=1
    print (ans)