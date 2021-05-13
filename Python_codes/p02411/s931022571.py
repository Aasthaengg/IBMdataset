while True:
    points = list(map(int,input().split()))

    if points == [-1,-1,-1]:
        break

    gou = points[0] + points[1]
    if points[0]==-1 or points[1]==-1:
        print("F")
    elif gou >= 80:
        print("A")
    elif 65 <= gou < 80:
        print("B")
    elif 50 <= gou < 65:
        print("C")
    elif 30 <= gou < 50:
        if points[2] >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")