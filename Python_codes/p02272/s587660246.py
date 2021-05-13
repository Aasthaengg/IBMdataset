#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def merge(A, left, mid, right):
    global count

    L = A[left:mid] + [1e9]
    R = A[mid:right] + [1e9]

    i, j = 0, 0

    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return None


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(int, _input[1].split()))
    assert array_length == len(array)
    count = 0
    merge_sort(A=array, left=0, right=array_length)
    print(*array)
    print(count)