mod = 2019
l,r = map(int,input().split())
INF = float("inf")
if (r-l) >= mod:
    print(0)
else:
    a = l % mod 
    b = r%mod
    if b > a:
        m = +INF
        for i in range(a,b+1):
            for j in range(i+1,b+1):
                curr = (i*j) % mod
                if curr < m:
                    m =curr
        print(m)
    else:
        print(0)