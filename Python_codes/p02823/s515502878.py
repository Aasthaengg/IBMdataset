n, a, b = map(int, input().split())

ans = 0
if (b-a)%2 == 0:
    print((b-a)//2)
else:
    ans = 0
    if (b-1) < (n-a):
        ans += a-1
        b -= a-1
        a = 1
        if (b-a)%2 != 0:
            ans += 1
            b -= 1
        ans += (b-a)//2
        print(ans)
    else:
        ans += n-b
        a += n-b
        b = n
        if (b-a)%2 != 0:
            ans += 1
            a += 1
        ans += (b-a)//2
        print(ans)