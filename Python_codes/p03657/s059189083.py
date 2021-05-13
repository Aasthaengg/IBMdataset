def resolve():
    a, b = map(int, input().split())

    ans = str()
    if a % 3 == 0 or b % 3 == 0 or (a+b) % 3 == 0:
        ans = "Possible"
    else:
        ans = "Impossible"
    
    print(ans)
resolve()