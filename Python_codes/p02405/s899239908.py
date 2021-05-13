while True :
    H, W = [int(temp) for temp in input().split()]
    
    if H == W == 0 :
        break
    
    for making in range(H):
        if making % 2 == 0 :
            if   W % 2 == 0 : print('#.' * (W // 2))
            else            : print('#.' * (W // 2) + '#')
        else :
            if   W % 2 == 0 : print('.#' * (W // 2))
            else            : print('.#' * (W // 2) + '.')

    print()