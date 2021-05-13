while(True):
    val1 = input().split(" ")
    m,f,r = [int(i) for i in val1]
    
    if m == -1 and f == -1 and r == -1:
        break
    

    n = m + f
    
    if m == -1 or f == -1:
        print("F")
    elif n >= 80:
        print("A")
    elif n >= 65:
        print("B")
    elif n >= 50:
        print("C")
    elif n >= 30:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")

