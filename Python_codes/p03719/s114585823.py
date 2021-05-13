def resolve():
    a, b, c = map(int, input().split())
    ans = str()

    if c >= a and c <= b:
        ans = "Yes"
    else:
        ans = "No"
    
    print(ans)
resolve()