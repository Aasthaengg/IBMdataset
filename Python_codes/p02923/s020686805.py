import sys
input = sys.stdin.readline
from collections import *

N = int(input())
H = list(map(int, input().split()))+[10**18]
ans = 0
cnt = 0

for i in range(N):
    if H[i]>=H[i+1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

print(ans)