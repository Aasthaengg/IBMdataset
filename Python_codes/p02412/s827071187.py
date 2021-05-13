while True:
    n,x= map(int,raw_input().split())

    if n == x == 0:
        break

    count = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                s = i + j + k
                if s == x:
                     count = count + 1
                     break
                elif s > x:
                     break
    print count