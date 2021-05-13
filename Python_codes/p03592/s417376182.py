#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, M, K = map(int, input().split())

for i in range(N + 1):
    for j in range(M + 1):
        k = i * M + j * N - i * j * 2
        if k == K:
            print("Yes")
            exit()

print("No")
