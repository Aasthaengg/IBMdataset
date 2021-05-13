while True:
    h,w = map(int, input().split())
    if h == 0 and w == 0:
        break
    else:
        a = ""
        b = ""
        for i in range(w):
            if i%2 == 0:
                a += "#"
                b += "."
            else:
                a += "."
                b += "#"
        for j in range(h):
            if j%2 == 0:
                print(a)
            else:
                print(b)
    print()
