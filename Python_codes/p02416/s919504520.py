while True:
    x = raw_input()
    if x == "0":
        break
    print("%d" % (sum(map(int, x)), ))
