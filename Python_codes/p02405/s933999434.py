def draw(h, w):
    for i in range(h):
        s = ""
        for j in range(w):
            s += ("#" if (i + j) % 2 == 0 else ".")
        print(s)
    print("")
 
while True:
    h, w = map(int, raw_input().split())
    if h == 0 and w == 0:
        break
    draw(h, w)