def resolve():
    x = int(input())
    a = int(input())
    b = int(input())
    ans = x - a
    while ans - b >= 0:
        ans -= b
    print(ans)
resolve()