while True:
    h, w = map(int, input().split(" "))
    if h == w == 0:
        break
    a = "#." * (w //2 + 1)
    for i in range(0,h):
        print((a[i%2:w+i%2]))
    print()