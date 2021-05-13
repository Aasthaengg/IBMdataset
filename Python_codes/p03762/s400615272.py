def resolve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x0 = x[0]
    y0 = y[0]
    x = list(map(lambda i:i-x0, x))
    y = list(map(lambda i:i-y0, y))
    sumx = sum(x)
    totalx = sumx
    for i in range(1,n):
        sumx -= (x[i]-x[i-1])*(n-i)
        totalx += sumx
        totalx %= ((10**9)+7)
    sumy = sum(y)
    totaly = sumy
    for i in range(1,m):
        sumy -= (y[i]-y[i-1])*(m-i)
        totaly += sumy
        totaly %= ((10**9)+7)
    print((totalx*totaly)%((10**9)+7))
resolve()