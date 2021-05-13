while True:
    s = raw_input()
    if s == "0":
        break
    print sum([int(i) for i in s])