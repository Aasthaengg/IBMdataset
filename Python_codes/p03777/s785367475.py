a, b = map(str, input().split())
if a == "H":
    print(b)
elif a == "D":
    if b == "H":
        print("D")
    elif b == "D":
        print("H")
