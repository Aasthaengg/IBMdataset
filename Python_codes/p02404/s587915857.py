# -*- coding:utf-8 -*-
while True:
    (H,W) = [int(s) for s in input().split()]
    if H == W == 0:
        break
    for i in range(H):
        if i ==0 or i == H-1:
            print('#'*W)
        else:
            print('#' + '.'*(W-2) + '#')
    print()