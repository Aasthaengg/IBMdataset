def aa096():
    a,b = list(map(int, input().split()))
    if a == b:
        print(a)
    elif a > b:
        print(a-1)
    else:
        print(a)

aa096()
