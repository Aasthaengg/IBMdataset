while True:
    H,W = map(int, input().split())
    if W == H == 0:
        break;
    L="#"*W
    for i in range(H):
        print(L)
    print("")