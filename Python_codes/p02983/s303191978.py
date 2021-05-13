import sys
import math
from collections import Counter


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())


l, r = inintm()

ans = 2019

for i in range(l, min(l+2019,r)):
    for j in range(i+1,min(l+2020,r+1)):
        if i*j % 2019 < ans:
            ans = i*j % 2019

print(ans)
