a=int(input())
b=list(map(int,input().split()))
"""
import statistics
import math
median = statistics.median(b) 中央値出そうとした
print(median)
"""
b.sort()
c=int(a/2)
print(b[c]-b[c-1])