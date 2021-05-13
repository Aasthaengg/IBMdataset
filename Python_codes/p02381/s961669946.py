# -*- coding: utf-8 -*-
# ITP1_10_C

import statistics

while 1:
    n = int(input())
    if n == 0 :
        break
    data = map(int, input().split())
    """
    statistics.m = mean(data)
    statistics.median = median(data)
    statistics.variance = variance(data)
    """
    std = float(statistics.pstdev(data))
    
    print(std)
    
