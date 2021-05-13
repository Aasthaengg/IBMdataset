def f02():
    k, x=map(int, input().split())
    s=x+1-k
    print(*[s+i for i in range(2*k-1)])

f02()