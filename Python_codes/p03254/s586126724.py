N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if sum(a) < x:
    print(N - 1)

elif sum(a) > x:
    ans = 0
    ans_ = 0
    for a in a:
        ans_ += a
        if ans_ > x:
            break
        ans += 1
    print(ans)

elif sum(a) == x:
    print(N)
