from sys import stdin
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction

n, k = map(int, input().split())
intensity = list(map(int, stdin.readline().split()))

count = 0
while count < k:
    totsum = 0
    prefs = [0]*n
    zeros = []
    for i in range(n):
        l = i - intensity[i]
        r = i + intensity[i] + 1

        prefs[max(l, 0)] += 1
        if r <= n-1: 
            prefs[r] += -1
            
    for i in range(1, n):
        prefs[i] += prefs[i-1]
        totsum += prefs[i]
    
    if sum(prefs) == n*n:
        print(*prefs)
        exit()
    
    intensity = prefs
    count += 1

print(*prefs)