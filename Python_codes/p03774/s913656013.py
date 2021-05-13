n,m = map(int,input().split())
a = [tuple(map(int,input().split())) for i in range(n)]
b = [tuple(map(int,input().split())) for i in range(m)]
inf = float("inf")
for ai,bi in a:
    d,num = inf,0
    for i in range(m):
        ci,di = b[i]
        x = abs(ai-ci)+abs(bi-di)
        if d > x:
            d = x
            num = i+1
    print(num)