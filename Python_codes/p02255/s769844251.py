# -*- coding: utf-8 -*-

N = int(raw_input())
A = map(int, raw_input().split())
for i in range(N):
    v = A[i]
    j = i-1
    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    print ' '.join(map(str, A))