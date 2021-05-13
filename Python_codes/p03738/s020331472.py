def resolve():
    a = int(input())
    b = int(input())

    ans = str()

    if a > b:
        ans = "GREATER"
    elif a < b:
        ans = "LESS"
    else:
        ans = "EQUAL"

    print(ans)
resolve()