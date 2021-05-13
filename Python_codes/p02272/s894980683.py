# -*- coding: utf-8 -*-

import sys

def merge(A, left, mid, right):
    global count
    n1 = mid-left
    n2 = right-mid
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = A[left+i]
    for i in range(n2):
        R[i] = A[mid+i]
    L[n1] = R[n2] = sys.maxint
    i = j = 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left+right)/2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

n = int(raw_input())
S = map(int, raw_input().split())
count = 0
mergeSort(S, 0, n)
print " ".join(map(str, S))
print count