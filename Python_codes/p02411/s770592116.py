while True:
    value = list(map(int, str(input()).split()))
    if value[0] == -1 and value[1] == -1 and value[2] == -1:
        break



    sum = value[0] + value[1]

    if value[0] == -1 or value[1] == -1:
        print("F")
    elif sum >= 80:
        print("A")
    elif sum >= 65:
        print("B")
    elif sum >= 50:
        print("C")
    elif value[2] >= 50:
        print("C")
    elif sum >= 30:
        print("D")
    else:
        print("F")


