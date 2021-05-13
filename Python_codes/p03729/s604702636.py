def resolve():
    a, b, c = input().split()

    ans = str()
    if a[-1] == b[0] and b[-1] == c[0]:
        ans = "YES"
    else:
        ans = "NO"
    
    print(ans)
resolve()