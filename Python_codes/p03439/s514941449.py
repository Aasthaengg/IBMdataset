import sys, heapq, bisect, math, fractions
from collections import deque
from collections import Counter
from collections import OrderedDict

N = int(input())

left = 0
right = N - 1
mid = 0

print(left, flush=True)
l = input()
if l == "Vacant":
    exit()
    
print(right, flush=True)
r = input()
if r == "Vacant":
    exit()

while left + 1 != right:
    mid = (right + left) // 2
    print(mid, flush=True)
    m = input()
    if m == "Vacant":
        exit()
        
    if ((mid - left) % 2 == 0 and l != m) or ((mid - left) % 2 == 1 and l == m):
        right = mid
        r = m
    else:
        left = mid
        l = m
