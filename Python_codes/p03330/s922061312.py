from collections import Counter
from itertools import permutations
import sys
input = sys.stdin.buffer.readline
N, C = map(int, input().split())
D = [[int(x) for x in input().split()] for _ in range(C)]

cnt = [Counter() for _ in range(3)]

for i in range(N):
    c = [int(x)-1 for x in input().split()]
    for j in range(3):
        cnt[j].update(c[(3-(i+2)+j)%3::3])

ans = 1000*500*500+5
for p in permutations(range(C), 3):
    s = 0
    for j in range(3):
        for k, v in cnt[j].items():
            s += D[k][p[j]] * v
    ans = min(ans, s)

print(ans)