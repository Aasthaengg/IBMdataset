while True:
    h, w=map(int, input().split())
    bod="#."*151
    if h == 0 and w==0: break
    for i in range(h):
        print(bod[i%2:i%2+w])
    print()
