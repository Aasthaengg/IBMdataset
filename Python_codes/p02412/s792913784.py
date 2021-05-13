while True:
    n,x = map(int,input().split())

    if n==0 and x==0:
        break

    print(sum( [ len(range(max(i+1,x-i-n),min(n,(x-i+1)//2))) for i in range(1,min(n-1,x//3)) ]))