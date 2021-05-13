#!/usr/bin/env python3
N = int(input())
V, M, F = "Vacant", "Male", "Female"
left = 0
right = N
print(0)
s_left = input()
if s_left == V:
    exit()
while True:
    mid = (right + left) // 2
    print(mid)
    s_mid = input()
    if s_mid == V:
        exit()
    if s_left == s_mid:
        if (mid - left) % 2:
            right = mid
        else:
            left = mid
    else:
        if (mid - left) % 2:
            left = mid
            s_left = s_mid
        else:
            right = mid
