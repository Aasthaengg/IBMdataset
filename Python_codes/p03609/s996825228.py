def resolve():
    x, t = map(int, input().split())
    ans = x-t

    if x-t < 0:
        ans = 0
    print(ans)
resolve()