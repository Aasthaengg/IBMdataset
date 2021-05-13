from sys import stdin
import math
import fractions
import heapq

n = int(stdin.readline().rstrip())

cnt = n * (n-1) // 2

print(cnt)