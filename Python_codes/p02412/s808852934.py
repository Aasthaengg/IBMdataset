while True:
    n, x = map(int, input().split())
    if n+x==0:
        break
    count=0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            a=x-(i+j)
            if a!=i and a!=j and a<=n and 0<a<i:
                count += 1
    print(count)