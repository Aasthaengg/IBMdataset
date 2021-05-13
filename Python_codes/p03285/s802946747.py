#!/usr/bin/env python3
n = int(input())

ans = False

for j in range(25):  #4$
        for k in range(15):  #7$
            if j + k == 0:
                continue
            if n % ((j * 4) + (k * 7)) == 0:
                ans = True
                break
        if ans:
            break

print("Yes" if ans else "No")
