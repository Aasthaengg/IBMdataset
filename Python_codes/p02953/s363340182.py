#!/usr/bin/env python3
n, *h = map(int, open(0).read().split())
for i in range(1, n):
    if h[-i] < h[-i - 1]:
        h[-1 - i] -= 1
        if h[-i] < h[-i - 1]:
            print("No")
            exit()
print("Yes")
