#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin

num_swap = 0


def merge(a, left, mid, right):
    global num_swap
    L = a[left:mid]
    R = a[mid:right]
    L.append(10**9+1)
    R.append(10**9+1)
    i = j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        num_swap += 1


def merge_sort(a, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)


stdin.readline()
s = [int(s) for s in stdin.readline().split()]
merge_sort(s, 0, len(s))
print(*s)
print(num_swap)