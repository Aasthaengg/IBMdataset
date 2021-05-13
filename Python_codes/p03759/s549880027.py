def resolve():
    a, b, c = map(int, input().split())

    ans = str()
    if b-a == c-b:
        ans = "YES"
    else:
        ans = "NO"
    
    print(ans)
resolve()