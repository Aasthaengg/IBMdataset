import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda t: t[0])
ans = 0

for A, B in AB:
    if M-B>=0:
        ans += A*B
        M -= B
    else:
        ans += A*M
        break

print(ans)