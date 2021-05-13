while True:
    line = input()
    data = line.split()
    h = int(data[0])
    w = int(data[1])
    if h == 0 and w == 0:
        break

    for i in range(h):   
        for j in range(w):
            if i%2 == 0:
                if j%2 == 0: 
                    print("#", end="")
                elif j%2 == 1:
                    print(".", end="")
            elif i%2 == 1:
                if j%2 == 0:
                    print(".", end="")
                elif j%2 == 1:
                    print("#", end="")
        print("")
    print("")





