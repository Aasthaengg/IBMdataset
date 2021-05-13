def resolve():
    a, b, t = map(int, input().split())
    time = a
    ans = 0
    while time <= t + 0.5:
        time += a
        ans += b
    print(ans)
resolve()