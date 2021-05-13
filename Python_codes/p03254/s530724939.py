n,x = map(int,input().split())
a = list(map(int,input().split()))
if sum(a) == x:
    print(n)
elif sum(a) < x:
    print(n-1)
else:
    a.sort()
    ans = 0
    for i in a:
        if i > x:
            break
        else:
            x -= i
            ans += 1
    print(ans)
