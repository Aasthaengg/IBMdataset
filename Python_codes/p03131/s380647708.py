k, a, b = map(int,input().split())

if b-a <= 2:
    print(k+1)
else:
    ans = a
    k -= a-1
    if k%2 == 0:
        ans += (b-a)*(k//2)
    else:
        ans += (b-a)*(k//2)
        ans += 1
    print(ans)