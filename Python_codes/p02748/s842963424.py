def resolve():
    A,B,M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    min_price = min(a) + min(b)
    for i in range (M):
        x,y,c = map(int,input().split())
        min_price = min(a[x-1] + b[y-1] - c, min_price)
    print(min_price)
resolve()