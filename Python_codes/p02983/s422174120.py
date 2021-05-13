l,r = map(int,input().split())
if r-l >= 2019:
    print(0)
else:
    r1 = r % 2019
    l1 = l % 2019
    if l1 > r1:
        print(0)
    else:
        ans = 2019
        for i in range(l1, r1):
            for j in range(i + 1, r1 + 1):
                ans = min(ans, (i*j) % 2019)
        print(ans)