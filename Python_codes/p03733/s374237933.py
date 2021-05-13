def resolve():
    n, time = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += min(t[i+1]-t[i], time)
    print(ans+time)
resolve()