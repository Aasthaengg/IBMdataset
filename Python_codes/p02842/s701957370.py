def resolve():
    x = int(input().strip())
    a =int( x // 1.08 )
    b =int( -1 * (-1 * x // 1.08))
    ans = ':('
    if int(a * 1.08) == x:
        ans = int(a)
    if int(b * 1.08) == x:
        ans = int(b)
    print(ans)
resolve()
