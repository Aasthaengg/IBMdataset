def resolve():
    a, b = map(int, input().split())

    ans = ""

    if a + b >= 10:
        ans = "error"
    else:
        ans = a + b
    
    print(ans)
resolve()