import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(M)]

for a, b in ab:
    m = min(abs(a-c)+abs(b-d) for c, d in cd)
    
    for i in range(M):
        if abs(a-cd[i][0])+abs(b-cd[i][1])==m:
            print(i+1)
            break
