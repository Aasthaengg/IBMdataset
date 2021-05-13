def resolve():
    n, m = map(int, input().split())
    if n == 1:
        print(3800)
    else:
        print((2**m)*(1900*m+100*(n-m)))
resolve()