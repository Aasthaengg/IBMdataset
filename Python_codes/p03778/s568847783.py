def resolve():
    w, a, b = map(int, input().split())

    a1 = a
    a2 = a + w

    b1 = b
    b2 = b + w

    ans = 0
    if a2 < b1:
        ans = b1 - a2
    elif b2 < a1:
        ans = a1 - b2
    else:
        ans = 0
    
    print(ans)

resolve()