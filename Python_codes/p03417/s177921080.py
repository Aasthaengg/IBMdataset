n,m = map(int,input().split())
mx = max(n,m)
mn = min(n,m)

if mn == 1:
    if mx == 1:
        print(1)
    else:
        print(mx - 2)
elif mn >= 2:
    print((mx - 2) * (mn - 2))
