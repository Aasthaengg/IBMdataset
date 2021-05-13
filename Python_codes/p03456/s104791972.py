def resolve():
    n = int(input().replace(" ", ""))
    if (n ** 0.5).is_integer():
        print("Yes")
    else:
        print("No")
resolve()