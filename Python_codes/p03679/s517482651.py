def resolve():
    x, a, b = map(int, input().split())

    ans = str()
    if a >= b:
        ans = "delicious"
    elif a+x >= b:
        ans = "safe"
    elif a+x < b:
        ans = "dangerous"
    print(ans)
resolve()