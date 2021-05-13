while True:
    x = input()
    if x.rstrip() == "0":
        break
    else:
        s = 0
        for c in x:
            s += int(c)
        print(s)