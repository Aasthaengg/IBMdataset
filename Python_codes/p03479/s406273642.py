def resolve():
    X, Y =map(int, input().split())
    ans = 1
    count = X
    while count*2 <= Y:
        ans += 1
        count *= 2
    print(ans)
resolve()