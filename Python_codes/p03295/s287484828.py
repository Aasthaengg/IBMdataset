import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from operator import itemgetter
N,M = map(int,readline().split())
m = map(int,read().split())
AB = zip(m,m)
AB = [(a,b) for a,b in AB]
AB.sort(key = itemgetter(1))
INF = 10 ** 18
prev_cut = -INF
cnt = 0
for a,b in AB:
    if a<=prev_cut:
        continue
    cnt += 1
    prev_cut = b-1
print(cnt)