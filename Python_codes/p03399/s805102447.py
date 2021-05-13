def resolve():
    ans = 0
    for i in range(2):
        a = int(input())
        b = int(input())
        if a < b:
            ans += a
        else:
            ans += b
    print(ans)
resolve()