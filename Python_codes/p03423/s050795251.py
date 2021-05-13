# -*- coding: utf-8 -*-
N = int(input())

if N <=2:
    print(0)
elif N % 3 == 0:
    print(int(N/3))
elif N % 3 == 1:
    print(int((N-1)/3))
elif N % 3 == 2:
    print(int((N-2)/3))
