def resolve():
    n = int(input())
    d = list(map(int, input().split()))
    d = sorted(d)
    if n%2 == 0: #偶数
        ans = d[n//2] - d[n//2 - 1]
    else: #奇数
        ans = 0
    print(ans)
resolve()