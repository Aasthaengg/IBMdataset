n,k = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)])
for a,b in ab:
    if b <= k:
        k -= b
    else:
        k = 0
    if k == 0:
        print(a)
        exit()