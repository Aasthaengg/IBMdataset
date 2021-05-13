def resolve():
    a, b, c = map(int, input().split())

    ans = str()
    x = a

    ans = str()
    for i in range(0, 100):
        if x > a + b:
            break
        if x > b:
            x = x % b
        if x == c:
            ans = "YES"
            break
        if i == 100 - 1:
            ans = "NO"
        ##print(f"{i} times {x} {x+a}")
        x += a
    print(ans)

resolve()