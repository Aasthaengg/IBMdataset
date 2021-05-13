#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

n = int(input())
a = list(map(int , input().split()))
print(2*n)
if a[np.argmax(a)] <= -a[np.argmin(a)]:
    cnt = len(a) - 1
    for i in range(0, len(a)):
        print(str(np.argmin(a) + 1) + " " + str(cnt + 1))
        a[cnt] += a[np.argmin(a)]
        print(str(np.argmin(a) + 1) + " " + str(cnt + 1))
        a[cnt] += a[np.argmin(a)]
        cnt -= 1;
else:
    cnt = 0
    for i in range(0, len(a)):
        print(str(np.argmax(a) + 1) + " " + str(cnt + 1))
        a[cnt] += a[np.argmax(a)]
        print(str(np.argmax(a) + 1) + " " + str(cnt + 1))
        a[cnt] += a[np.argmax(a)]
        cnt += 1
