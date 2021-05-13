while True :
    H, W = [int(temp) for temp in input().split()]
    
    if H == W == 0 :
        break
    
    for making in range(H):
        print('#' * W)

    print()