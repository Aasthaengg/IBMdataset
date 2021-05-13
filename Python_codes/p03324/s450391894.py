# -*- coding: utf-8 -*-

D, N = map(int, input().split())

if (100 ** D * N) / 100 != 100 ** D:
    print(100 ** D * N)
else:
    print((100 ** D * N) + (100 ** D))