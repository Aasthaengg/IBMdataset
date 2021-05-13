import math
import re
import copy
import sys

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0

for i in range(n):
    c += min(a[i],b[i])
    if a[i] < b[i]:
        c += min(a[i+1],b[i]-a[i])
        a[i+1] -= min(a[i+1],b[i]-a[i])

print(c)