while True:
    n,x=map(int,input().split())
    if n==x==0:
        break
    ans = 0
    for n1 in range(1, n+1):
        if n1 > x:
            break
        for n2 in range(n1+1, n+1):
            for n3 in range(n2+1, n+1):
                if n1 + n2 + n3 == x:
                    ans += 1
    print(ans)

