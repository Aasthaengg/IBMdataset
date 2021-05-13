n, x = map(int,input().split())
l = list(map(int,input().split()))
if sum(l) <= x:
    print(n+1)
else:
    i, d = 0, 0
    while i<n and d <= x:
        d += l[i]
        i += 1
    if d == x and i == n:
        print(i+1)
    else:
        print(i)