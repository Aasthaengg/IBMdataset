# coding: utf-8

import math

ans = []

while True:
    if int(input()) == 0:
        break
    data = list(map(int, input().strip().split()))
    ave_data = sum(data) / len(data)
    ans += [math.sqrt(sum([(i - ave_data) ** 2 for i in data]) / len(data))]
    
print('\n'.join(map(str, ans)))