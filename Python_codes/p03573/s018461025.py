def resolve():
    a, b, c = map(int, input().split())

    ans = 0
    if b == c: ans = a
    elif a == c: ans = b
    elif a == b: ans = c
    print(ans)
resolve()