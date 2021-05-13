# coding: utf-8
import math
n = int(input())
t = 0
x = 0
y = 0
txy = []
for i in range(n):
    ti, xi, yi = list(map(int, input().split()))
    txy.append((ti, xi, yi))

for ti, xi, yi in txy:
    if abs(xi - x) + abs(yi - y) > abs(ti - t):
        print("No")
        exit()
    elif (abs(xi - x) + abs(yi - y) - abs(ti - t)) % 2 != 0:
        print("No")
        exit()
    else:
        t = ti
        x = xi
        y = yi
print("Yes")
