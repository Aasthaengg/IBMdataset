n, x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
if sum(a) < x:
    print(n-1)
    exit()
    
elif sum(a) == x:
    print(n)
    exit()
    
else:
    a = sorted(a)
    for i in range(n):
        ans += a[i]
        if ans > x:
            print(i)
            exit()