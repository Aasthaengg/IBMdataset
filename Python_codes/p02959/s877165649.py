def abc135c():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        v = min(b[i], a[i])
        ans += v
        b[i] -= v
        vv = min(a[i+1], b[i])
        a[i+1] -= vv
        ans += vv
    print(ans)
abc135c()