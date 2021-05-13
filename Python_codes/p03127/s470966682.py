#!/usr/bin/env python
import sys 
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n): 
    ans = math.gcd(ans, a[i])

print(ans)
