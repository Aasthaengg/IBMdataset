L, R = map(int, input().split())
if R - L >= 673:
    print(0)
elif R - L == 1:
    print((R*L)%2019)
else:
    L %= 2019
    R %= 2019
    if L > R:
        print(0)
    else:
        ans = (L*R)%2019
        for l in range(L, R):
            for r in range(l+1, R+1):
                val = (l*r)%2019
                ans = min(ans, val)
        print(ans)