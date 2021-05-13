# 2020/07/23
# AtCoder Beginner Contest 126 - C
import math

# Input
n, k = map(int,input().split())

ans = 0

# Calc
for i in range(1, n+1):
    idx = 1
    wval = i
    while(wval < k):
        wval = wval * 2
        idx = idx + 1
    
    ans = ans + (1/n) * (1/2) ** idx

# Output
print(ans*2)
