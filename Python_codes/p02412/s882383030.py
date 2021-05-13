while True:
    count=0
    n, s = tuple([int(x) for x in raw_input().split(" ")])

    if n==0 and s==0:
        break
    
    for i in range(1, n-1):
        for j in range(i+1, n):
            r = s - (i + j)
            if j < r and r <= n:
                count+=1
    print count