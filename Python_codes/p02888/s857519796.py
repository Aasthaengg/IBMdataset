#!/usr/bin/env python3
N = int(input())
L = sorted([int(s) for s in input().split()])


def check_search(middle, idx_short2, l_lng, l_lows):
    return l_lows[middle] + l_lows[idx_short2] > l_lng


l_lows = L[:2]
triangles = 0


for l_lng in L[2:]:
    for idx, l_low in enumerate(l_lows):
        left = 0
        right = len(l_lows) - 1 - idx
        end = right
        while (left < right):
            middle = (left + right) // 2
            if check_search(middle, len(l_lows) - 1 - idx, l_lng, l_lows):
                right = middle
            else:
                left = middle + 1
        triangles += (end - right)
    l_lows.append(l_lng)

print(triangles)