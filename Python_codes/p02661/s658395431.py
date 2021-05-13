n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

if n % 2:

    ab.sort()
    l = ab[(n+1)//2-1][0]

    ab.sort(key=lambda x:x[1], reverse=True)
    r = ab[(n+1)//2-1][1]

    print(r-l+1)

else:

    a = [ai for ai, bi in ab]
    b = [bi for ai, bi in ab]

    a.sort()
    b.sort()

    ll = a[n//2-1]
    lr = b[n//2-1]

    rl = a[n//2]
    rr = b[n//2]


    print((lr+rr) - (ll+rl) + 1)