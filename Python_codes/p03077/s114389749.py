#!/usr/bin/env python
import sys 
import math
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(5)]
ans = math.ceil(n/min(a)) + 4 
print(ans)
