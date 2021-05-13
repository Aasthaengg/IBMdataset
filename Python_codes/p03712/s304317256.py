# -*- coding: utf-8 -*-
H, W = map(int, input().split())
print('#' * (W + 2) )
for _ in range(H):
    print("#{}#".format(input()))
print('#' * (W + 2) )
