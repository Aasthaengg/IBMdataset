n,x = map(int,input().split())
a = list(map(int,input().split()))
if sum(a) == x:
    print(n)
elif sum(a) < x:
    print(n - 1)
else:
    ans = 0
    a.sort()
    for i in range(n):
        if a[i] > x:
            break
        else:
            x -= a[i]
            ans += 1
    print(ans)