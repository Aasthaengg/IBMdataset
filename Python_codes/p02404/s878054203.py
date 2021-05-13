while True:
    (H, W) = [int(i) for i in input().split()]
    if H == W == 0:
        break

    [print('#' * W) if i == 0 or i == H - 1 else print('#'+'.'*(W-2)+'#')
            for i in range(H)]
    print()