import sys
input = sys.stdin.readline
from collections import *

N = int(input())
a = list(map(int, input().split()))
cnt = [0]*9

for ai in a:
    i = min(ai//400, 8)
    cnt[i] += 1

m = 0
M = 0

for i in range(8):
    if cnt[i]>0:
        m += 1
        M += 1

if cnt[-1]>0:
    if m==0:
        m = 1
    
    M += cnt[-1]

print(m, M)