import sys
input = sys.stdin.buffer.readline

from collections import defaultdict

H, W, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

counter = defaultdict(int)
for a, b in AB:
  for aa in range(a - 1, a + 2):
    for bb in range(b - 1, b + 2):
      if 2 <= aa <= H - 1 and 2 <= bb <= W - 1:
        counter[(aa, bb)] += 1

answer = [0] * (10)
for (x, y), n in list(counter.items()):
  if n:
    answer[n] += 1
answer[0] = (H - 2) * (W - 2)
for i in range(1, 10):
  answer[0] -= answer[i]
  
for a in answer:
  print(a)