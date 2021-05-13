# -*- coding: utf-8 -*-
n = int(input())
h = list(reversed(list(map(int, input().split()))))

cnt = 0
for i in range(n-1):
    if h[i+1] - h[i] > 1:
        print('No')
        exit(0)
    elif h[i+1] - h[i] == 1:
        h[i+1] -= 1

print('Yes')
