a, b = input().split()
if a == "H":
    if b == "H":
        print("H")
    if b == "D":
        print("D")
if a == "D":
    if b == "H":
        print("D")
    if b == "D":
        print("H")