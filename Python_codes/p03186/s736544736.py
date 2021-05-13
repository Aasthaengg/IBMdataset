# -*- coding: utf-8 -*-
data = list(map(int, input().split()))
if data[0] + data[1] >= data[2] - 1:
    print(data[1] + data[2])
else:
    print(2 * data[1] + data[0] + 1)