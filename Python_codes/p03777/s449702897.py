a,b = map(str,input().split())
if a == "H":
    if b == "H":
        print("H")
    elif b =="D":
        print("D")
if a == "D":
    if b =="H":
        print("D")
    elif b == "D":
        print("H")