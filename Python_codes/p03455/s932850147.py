def resolve():
    a, b = map(int, input().split())
    c = a*b
    ans = ""
    if c % 2 == 0:
        ans = "Even"
    else:
        ans = "Odd"
    print(ans)
resolve()