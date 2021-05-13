def resolve():
    n, a, b = map(int, input().split())

    if a*n <= b:
        ans = a*n
    else:
        ans = b
    print(ans)
resolve()