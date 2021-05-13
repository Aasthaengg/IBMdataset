while True:
    inps = input().split()
    if len(inps) < 3:
        print("Illegal input.")
        break
    else:
        a = int(inps[0])
        b = int(inps[2])
        if inps[1] == "+":
            print(a + b)
        elif inps[1] == "-":
            print(a - b)
        elif inps[1] == "*":
            print(a * b)
        elif inps[1] == "/":
            print(a // b)
        elif inps[1] == "?":
            break
        else:
            print("Illegal input.")
            break