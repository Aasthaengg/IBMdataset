import sys
input = sys.stdin.readline
from collections import *

N = int(input())
a = list(map(int, input().split()))
ans = 0

for ai in a:
    while ai%2==0:
        ai //= 2
        ans += 1

print(ans)