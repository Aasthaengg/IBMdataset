# Allocation
from collections import deque

n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]


def can_load(P):
    num_track = 1
    load = 0
    for w in W:
        if w > P:
            return False

        if load + w > P:
            if num_track == k:
                return False

            num_track += 1
            load = w

        else:
            load += w

    return True


def binary_search():
    top = 0
    bottom = sum(W)+1

    while top < bottom:
        mid = (top+bottom)//2

        if can_load(P=mid):
            bottom = mid
        else:
            top = mid + 1

    return top


print(binary_search())

