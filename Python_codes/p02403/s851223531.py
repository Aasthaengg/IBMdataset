while True:
    H, W = list(map(int, input().split()))
    if (H == 0) & (W == 0):
        break
    for _ in range(H):
        print(W * "#")
    print("")