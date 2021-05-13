while True:
    test = [int(score) for score in input().split(" ")]
    m = test[0]
    f = test[1]
    r = test[2]
   
    if m == f == -1:
        break
    elif m == -1 or f == -1:
        print("F")
    elif m + f >= 80:
        print("A")
    elif 65 <= m + f < 80:
        print("B")
    elif 50 <= m + f < 65:
        print("C")
    elif 30 <= m + f < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")