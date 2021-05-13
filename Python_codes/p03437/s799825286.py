#!/usr/bin/env python

x, y = map(int, input().split())
tmp = x 

if x%y == 0:
    print(-1)
    exit()

while True:
    x += tmp 
    if x%y != 0:
        print(x)
        exit()
