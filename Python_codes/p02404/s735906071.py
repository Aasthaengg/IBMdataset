while True:
       (H, W) = [int(x) for x in input().split()]
       if H == W == 0:
           break
       
       for hc in range(H):
             for wc in range(W):
                   if hc == 0 or hc == H - 1 or wc == 0 or wc == W - 1:
                         print('#', end='')
                   else:
                         print('.', end='')                                         
             print()     
       print()