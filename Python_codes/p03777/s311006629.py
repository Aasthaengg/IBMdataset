def resolve():
    a, b = input().split()

    ans = str()
    if a == "H":
        if b == "H":
            ans = "H"
        elif b == "D":
            ans = "D"
    elif a == "D":
        if b == "H":
            ans = "D"
        elif b == "D":
            ans = "H"
    
    print(ans)

resolve()