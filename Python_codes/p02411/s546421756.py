fn = lambda x : m+f >= x 
while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    if m == -1 or f == -1:
        print("F")
    elif fn(80):
        print("A")
    elif fn(65):
        print("B")
    elif fn(50):
        print("C")
    elif fn(30):
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")



