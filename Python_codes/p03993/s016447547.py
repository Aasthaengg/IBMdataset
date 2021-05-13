import sys
input = sys.stdin.readline
from collections import *

N = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(N):
    if a[a[i]-1]-1==i:
        ans += 1

print(ans//2)