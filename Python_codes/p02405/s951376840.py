h, w = map(int, input().split())
toggle = True
while h != 0:
    # print off the chess board
    for i in range(h):
        for j in range(w):
            char = "#" if (i+j) % 2 == 0 else "."
            print(char, end="")
        print()
    h, w = map(int, input().split())
    print()

