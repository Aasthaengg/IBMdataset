from collections import defaultdict, Counter
import sys
import itertools
input = sys.stdin.readline

c = defaultdict(int)
H,W,N = map(int,input().split())
for _ in range(N):
  a,b = map(int,input().split())
  # そのセルを含む正方形の中心を記録
  for dx,dy in itertools.product([-1,0,1],repeat = 2):
    aa = a + dx
    bb = b + dy
    if 2 <= aa <= H-1 and 2 <= bb <= W-1:
	    c[(aa,bb)] += 1

result = Counter(c.values())
result[0] = (H-2)*(W-2) - sum(result.values())

for j in range(10):
  print(result[j])
