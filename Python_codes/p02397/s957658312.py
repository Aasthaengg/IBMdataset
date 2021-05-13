while True:
    x = input()
    x = x.split(" ")
    x = [int(z) for z in x]
    if x[0] == 0 and x[1] == 0: break
    if x[0] < x[1]:
        print("%d %d" % (x[0], x[1]))
    else:
        print("%d %d" % (x[1], x[0]))