#!/usr/bin/env python3

H,W = [int(i) for i in input().split()]
F = []
F.append("."*(W+2))
for i in range(H):
    F.append("."+input()+".")
F.append("."*(W+2))

flg = True
for y in range(1,H+1):
    for x in range(1,W+1):
        if F[y][x] == '.':
            continue
        elif F[y-1][x] != '#' and F[y+1][x] != '#' and F[y][x-1] != '#' and F[y][x+1] != '#':
            flg = False
            break
if flg:
    print("Yes")
else:
    print("No")

            

