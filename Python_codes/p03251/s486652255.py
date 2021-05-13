#!/usr/bin/env python3
n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
max_x = max(x)
min_y = min(y)
for i in range(X + 1, Y):
    if i > max_x and i <= min_y:
        print("No War")
        exit()
print("War")