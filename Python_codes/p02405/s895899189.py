while 1:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    elif W % 2 == 0:
        s = "#." * (W // 2)
    elif W % 2 == 1:
        s = '#.' * (W // 2) + '#'
    for i in range(H):
        print(s)
        s = s.translate(str.maketrans('#.', '.#'))
    print()