while True:
    m,f,r = map(int, input().split())
    if m == f == r ==-1:
        break
    elif (m+f) >= 80:
        print("A")
    elif (m+f) < 80 and (m+f) >= 65:
        print("B")
    elif ((m+f) < 65 and (m+f) >= 50) or (((m+f) < 50 and (m+f) >= 30 and (m != -1 and f != -1)) and r >= 50):
        print("C")
    elif (m+f) < 50 and (m+f) >= 30 and (m != -1 and f != -1):
        print("D")
    else:
        print("F")
