while True:
    x = raw_input()
    if x == "0":
        break
    else:
        num = 0
        for i in x:
            num+=int(i)
        print num
