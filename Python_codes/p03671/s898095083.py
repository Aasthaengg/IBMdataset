def resolve():
    a = list(map(int, input().split()))
    a.sort()

    ans = a[0] + a[1]

    print(ans)
resolve()