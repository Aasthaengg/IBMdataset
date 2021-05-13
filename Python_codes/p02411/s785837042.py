m,f,r = 0,0,0
while True:
    m,f,r = [int(i) for i in input().split()]
    if m+f+r == -3:
        break
    elif -1 in {m,f}:
        print("F")
    elif 80 <= m+f:
        print("A")
    elif 65 <= m+f <= 80:
        print("B")
    elif 50 <= m+f <= 65:
        print("C")
    elif 30 <= m+f <= 50:
        if 50 <= r:
            print("C") 
        else:
            print("D")
    elif m+f <= 30:
        print("F")