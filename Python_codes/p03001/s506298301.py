#!/usr/bin/env python3
W,H,X,Y=map(int,input().split())
m = W*H/2
i = 0
if W%2 < 1 and H%2 < 1 and W//2 == X and H//2 == Y:
    i = 1
print(m,i)
