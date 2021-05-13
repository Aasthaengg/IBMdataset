while True:
    n=int(input())
    import statistics
    if n==0:
        break
    s=list(map(int,input().split()))
    x=float('{:.6f}'.format(statistics.pstdev(s))) 
    print(x)
