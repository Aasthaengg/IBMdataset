# coding: utf-8
# Your code here!

import math

while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    
    ave = sum(s)/n
    a2 = 0
    for i in range(n):
        a2 += (s[i]-ave)**2
    
    print(math.sqrt(a2/n))
