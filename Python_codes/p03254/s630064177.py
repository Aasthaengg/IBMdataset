def resolve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    a = sorted(a)
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        ans += 1
    if x != 0:
        ans -= 1
    print(ans)
resolve()