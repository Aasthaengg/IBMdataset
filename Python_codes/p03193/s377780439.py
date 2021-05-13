###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N, H, W = mi()

cnt = 0
for _ in range(N):
  a, b = mi()
  if a >= H and b >= W:
    cnt += 1

print(cnt)

